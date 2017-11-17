#!/usr/bin/python
#-------------------------------------------------------------------------------
# Name:        photobooth
# Purpose:     Program for photoboxes
#
# Author:      VoRoN
#
# Created:     03.10.2017
# Copyright:   (c) VoRoN 2017
# Licence:     MIT
#-------------------------------------------------------------------------------

import os, glob, sys
os.chdir(os.path.dirname(sys.argv[0]))
os.environ['PYGAME_FREETYPE'] = ''
import pygame
import widgets
import json
from PIL import Image, ImageDraw, ImageFont
import threading, thread
import datetime
import camera
import subprocess
from pygame_vkeyboard import *
from shutil import copy
import re

WIN32 = (os.name != 'posix')
TMP_FOLDER = 'tmp'
if not WIN32:
	TMP_FOLDER = '/tmp'
SETTINGS = {}
SCENES = []
PHOTO_FORMAT = []
screens = []
current_screen = 0
result_file_name = ''
TAKE_PHOTO = 4
photo_count = 1
thread_take_photo = None

delayScreen = 'Screen5'

done = False
COLLAGE = None
py_image = None

def getFilePath(filename):
	in_tmp_folder = os.path.join(TMP_FOLDER, filename)
	in_img_folder = os.path.join('img', filename)
	in_formats_folder = os.path.join('formats', filename)
	if os.path.exists(in_img_folder):
		return in_img_folder
	if os.path.exists(in_tmp_folder):
		return in_tmp_folder
	if os.path.exists(in_formats_folder):
		return in_formats_folder

def current_screen_is(name):
	if current_screen >= len(screens):
		return False
	return screens[current_screen].name == name

def previos_screen_is(name):
	if current_screen >= len(screens) or\
		current_screen - 1 < 0:
		return False
	return screens[current_screen - 1].name == name

def set_current_screen(name):
	global current_screen
	for x in xrange(len(screens)):
		if screens[x].name == name:
			current_screen = x
			break

def get_screen_by_name(name):
	for x in xrange(len(screens)):
		if screens[x].name == name:
			return screens[x]
	return None

def next_screen():
	global current_screen
	current_screen += 1

def create_photo(photo_config):
	if not WIN32:
		filepattern = os.path.join(TMP_FOLDER, 'capt%04n.jpg')
		camera.get_all_files(filepattern)
		thread.start_new_thread(camera.delete_all_files, ())
		
	scale = 2
	photo_format = tuple(map(lambda x: photo_config['dpi'] * x * scale,
													photo_config['format']))
	
	image = Image.new('RGB', photo_format,
									tuple(photo_config['background_color']))
	
	for item in photo_config['components']:
		item_type = item['type']
		
		if item_type == 'image':
			picture = item
			photo_name = getFilePath(picture['file'])
			photo = Image.open(photo_name)
			photo = photo.resize((picture['size'][0] * scale,
								  picture['size'][1] * scale))
			photo = photo.convert('RGBA')
			photo = photo.rotate(picture['angle'], expand=True)
			image.paste(photo, (picture['position'][0] * scale,
								picture['position'][1] * scale), photo)
			del photo
			
		if item_type == 'label':
			text_line = item['text']
			font = ImageFont.truetype(item['font'], item['font_size'] * scale)
			d = ImageDraw.Draw(image)
			size = d.textsize(text_line, font)
			
			text = Image.new('RGBA', size, (255, 255, 255, 0))
			dt = ImageDraw.Draw(text)
			dt.text((0, 0), text_line, tuple(item['text_color']), font)
			text = text.rotate(item['angle'], expand=True)
			
			x, y = item['position'][0] * scale, item['position'][1] * scale
			width, height = photo_format
			textWidth, textHeight = text.size
			
			if item['vertical_center']:
				y = height / 2 - textHeight / 2
			if item['horizontal_center']:
				x = width / 2 - textWidth / 2
			
			image.paste(text, (x, y), text)
			
			del d
			del dt
	
	today = datetime.datetime.today()
	path = 'results'
	if not os.path.exists(path):
		os.mkdir(path)
	filename = os.path.join(path, 'result_%s_%s.jpg' %
				(today.date().isoformat(), today.time().strftime('%H-%M-%S')))
	image.save(filename)
	global result_file_name
	result_file_name = filename
	
	if SETTINGS['preview_screen']:
		screen = get_screen_by_name('PreviewScreen')
		preview_picture = screen.getControlByName('preview')
		return image.resize(tuple(preview_picture.size)).transpose(Image.ROTATE_90)
	else:
		return None
			
def capture_photo(number):
	if not WIN32:
		camera.trigger_capture()

def checkPassword(password):
	global passKeyb
	if password.find('1532') > -1:
		passKeyb.disable()
		passKeyb.buffer = ''
		set_current_screen('OptionsScreen')
		updown = screens[current_screen].getControlByName("txtUpDown")
		updown.setText(str(SETTINGS['print_copies']))
		caption = screens[current_screen].getControlByName("txtCaption")
		caption.setText(SETTINGS['custom_text'])
		lblCollages = screens[current_screen].getControlByName("lblCollages")
		lblSaved = screens[current_screen].getControlByName("lblSaved")
		path = 'results'
		numfiles = len(glob.glob(path + '/*.jpg'))
		lblCollages.setText('Collages created: %d' % numfiles)
		lblSaved.setText('Saved: 0\\%d' % numfiles)
		
				
def main():
	global WIN32, TMP_FOLDER, SETTINGS, SCENES, PHOTO_FORMAT, screens,\
		current_screen, result_file_name, TAKE_PHOTO, photo_count,\
		thread_take_photo, delayScreen, done, COLLAGE, py_image
	
	with open('config.json', 'r') as f:
		SCENES = json.loads(f.read())
	with open('settings.json', 'r') as f:
		SETTINGS = json.loads(f.read())
	for fileName in os.listdir('formats'):
		with open(getFilePath(fileName), 'r') as f:
			frmt = json.loads(f.read())
			if isinstance(frmt, list):
				PHOTO_FORMAT += frmt
			else:
				PHOTO_FORMAT.append(frmt)
			
	
	pygame.init()
	pygame.mouse.set_visible(SETTINGS['show_mouse'])
	
	selected_format = PHOTO_FORMAT[0]

	for frmt in PHOTO_FORMAT:
		if frmt['name'] == SETTINGS['print_format']:
			selected_format = frmt
	selected_format['components'][-1]['text'] = SETTINGS['custom_text']
	
	font_cache = widgets.FontCache()
	image_cache = widgets.ImageCache()
	for item in SCENES:
		screens.append(widgets.Screen(item, font_cache, image_cache))
	
	window_prop = pygame.HWSURFACE
	if not WIN32:
		window_prop |= pygame.FULLSCREEN
	
	window = pygame.display.set_mode((800, 480), window_prop, 32)
	clock = pygame.time.Clock()
	
	global passKeyb
	passKeyb = VKeyboard(window, checkPassword,
						VKeyboardLayout(VKeyboardLayout.NUMBER),
						renderer=widgets.MyKeyboardRenderer.DEFAULT)
	
	delayScreen = SETTINGS['delay_screens']
	set_current_screen('MainScreen')
	while done == False:
		for event in pygame.event.get():
			if passKeyb.state == 0:
				screens[current_screen].onevent(event)
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if event.pos[1] < 240:
					passKeyb.disable()
				continue;
				 
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_ESCAPE:
					done = True
			if event.type == pygame.QUIT:
				done = True
			if event.type == pygame.MOUSEBUTTONUP and current_screen_is('PreviewScreen')\
				and SETTINGS['preview_screen_delay'] == 0:
				set_current_screen('EndScreen')
				pygame.time.set_timer(pygame.USEREVENT + 1, 5000)
	
			if event.type == pygame.USEREVENT + 1:
				next_screen()
				
				if current_screen_is('StrikeAPoseScreen'):
					if thread_take_photo != None:
						thread_take_photo.join()
					t = threading.Thread(target=capture_photo, args=(photo_count, ))
					thread_take_photo = t
					t.start()
					pygame.time.set_timer(pygame.USEREVENT + 1, 
											SETTINGS['strike_a_pose_delay'])
				
				if current_screen_is('PreviewScreen') and photo_count < TAKE_PHOTO:
					photo_count += 1
					if photo_count <= TAKE_PHOTO:
						set_current_screen(delayScreen)
						pygame.time.set_timer(pygame.USEREVENT + 1, 1000)
						
				if previos_screen_is('WorkInProgress') and COLLAGE == None:
					pygame.time.set_timer(pygame.USEREVENT + 1, 0)
					if thread_take_photo != None:
						thread_take_photo.join()
					COLLAGE = create_photo(selected_format)
					
					py_image = None
					if COLLAGE != None:
						mode = COLLAGE.mode
						size = COLLAGE.size
						data = COLLAGE.tobytes()
						py_image = pygame.image.fromstring(data, size, mode)
					
					if SETTINGS['preview_screen']:
						set_current_screen('PreviewScreen')
					else:
						set_current_screen('EndScreen')
						
					if SETTINGS['preview_screen_delay'] != 0\
						and SETTINGS['preview_screen']:
						pygame.time.set_timer(pygame.USEREVENT + 1,
												SETTINGS['preview_screen_delay'])
												
				if current_screen_is('WorkInProgress') and py_image == None\
					and COLLAGE != None:
						set_current_screen('EndScreen')
	
				if current_screen_is('PreviewScreen') and photo_count >= TAKE_PHOTO:
					if COLLAGE != None:
						picture = screens[current_screen].getControlByName('preview')
						picture.image = py_image
						py_image = None
					else:
						pygame.time.set_timer(pygame.USEREVENT + 1, 100)
						set_current_screen('WorkInProgress')
	
				if current_screen_is('EndScreen'):
					pygame.time.set_timer(pygame.USEREVENT + 1,
											SETTINGS['end_screen_delay'])
	
				if current_screen == len(screens):
					pygame.time.set_timer(pygame.USEREVENT + 1, 0)
					set_current_screen('MainScreen')
					
			if event.type == widgets.Button.EVENT_BUTTONCLICK:
				if event.name == 'btnStartClick':
					if not WIN32:
						camera.check_and_close_gvfs_gphoto()
					set_current_screen(delayScreen)
					pygame.time.set_timer(pygame.USEREVENT + 1, 1000)
					photo_count = 1
					thread_take_photo = None
					COLLAGE = None
					py_image = None
					result_file_name = ''
					
				if event.name == 'btnPrintClick':
					print 'Print photo'
					sub = subprocess.Popen(['lp', '-n',
								str(SETTINGS['print_copies']), '-d',
								'MITSUBISHI_CPD80D', result_file_name],
								stdout=subprocess.PIPE, stderr=subprocess.PIPE,
								shell=False)
					err = sub.stderr.read()
					print err
					
				if event.name == 'btnPrintAllClick':
					path = 'results'
					files = glob.glob(path + '/*.jpg')
					for f in files:
						sub = subprocess.Popen(['lp', '-n', str(1),
								'-d', 'MITSUBISHI_CPD80D', f],
								stdout=subprocess.PIPE, stderr=subprocess.PIPE,
								shell=False)
						err = sub.stderr.read()
						print err
				
				if event.name == 'btnOptionsClick':
					if current_screen_is('OptionsScreen'):
						updown = screens[current_screen].getControlByName("txtUpDown")
						SETTINGS['print_copies'] = int(updown.getText())
						caption = screens[current_screen].getControlByName("txtCaption")
						SETTINGS['custom_text'] = caption.getText()
						selected_format['components'][-1]['text'] = SETTINGS['custom_text']
						with open('settings.json', 'w') as f:
							f.write(json.dumps(SETTINGS, indent=4))
						set_current_screen('MainScreen')
					else:
						passKeyb.enable()
				
				if event.name == 'btnUpClick':
					ctrl = screens[current_screen].getControlByName("txtUpDown")
					value = int(ctrl.getText())
					ctrl.setText(str(value + 1))
					
				if event.name == 'btnDownClick':
					ctrl = screens[current_screen].getControlByName("txtUpDown")
					value = int(ctrl.getText())
					if value > 1:
						ctrl.setText(str(value - 1))
				
				if event.name == 'btnSaveClick':
					reg = re.compile('sda\d')
					dev = ''
					with open('/proc/partitions') as f:
						parts = f.readlines()
						parts = parts[2:]
						for part in parts:
							rows = part.split()
							if reg.search(rows[3]):
								dev = rows[3]
								break
					dest = ''
					regmt = re.compile(dev)
					mount = subprocess.Popen(['mount'], stdout=subprocess.PIPE,
									shell=False)
					mounts = mount.stdout.readlines()
					for mpoint in mounts:
						points = mpoint.split()
						if regmt.search(points[0]):
							dest = points[2]

					if dest != '':
						path = 'results'
						lblSaved = screens[current_screen].getControlByName("lblSaved")
						files = glob.glob(path + '/*.jpg')
						numfiles = len(files)
						saved = 0
						for f in files:
							copy(f, dest)
							saved += 1
							lblSaved.setText('Saved: %d\\%d' % (saved, numfiles))
							## hack, update screen
							screens[current_screen].render(window)
							pygame.display.flip()
					
		screens[current_screen].render(window)
		for textedit in \
			screens[current_screen].getControlsByType(widgets.TextEdit):
			if textedit.keyboard.state > 0:
				textedit.keyboard.invalidate()
				textedit.keyboard.on_event(event)
		if passKeyb.state > 0:
			passKeyb.invalidate()
			passKeyb.on_event(event)
			
		pygame.display.flip()
		clock.tick(60)
	pygame.quit()
	
if __name__ == '__main__':
    main()