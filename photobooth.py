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

import os
os.environ['PYGAME_FREETYPE'] = ''
import pygame
from virtualKeyboard import VirtualKeyboard
import widgets
import json
from PIL import Image, ImageDraw, ImageFont
import threading, thread
import datetime
import camera

SETTINGS = {
	'print_format':'4x6',
	'delay_screens':'Screen1',
	'strike_a_pose_delay':2000,
	'preview_screen':True,
	'preview_screen_delay':0,
	'end_screen_delay':5000
}

WIN32 = (os.name != 'posix')

SCENES = []
with open('config.json', 'r') as f:
	SCENES = json.loads(f.read())

pygame.init()
#pygame.mouse.set_visible(0)

screens = []
current_screen = 0
TMP_FOLDER = 'tmp'

for item in SCENES:
	screens.append(widgets.Screen(item))

window_prop = pygame.HWSURFACE
if not WIN32:
	window_prop = pygame.FULLSCREEN
	TMP_FOLDER = '/tmp'

window = pygame.display.set_mode((800, 480), window_prop, 32)
clock = pygame.time.Clock()

def create_photo():
	if not WIN32:
		filepattern = os.path.join(TMP_FOLDER, 'capt%04n.jpg')
		camera.get_all_files(filepattern)
		thread.start_new_thread(camera.delete_all_files, ())
	
	F4x6 = (4 * 300, 6 * 300)
	image = Image.new('RGB', F4x6, (255, 255, 255))
	positions = [(100, 120), (100, 120 + 750 + 60), (100 + 60 + 500, 120),\
				(100 + 60 + 500, 120 + 750 + 60)]
	for i in xrange(1, 5):
		photo = Image.open(os.path.join(TMP_FOLDER, 'capt000%d.jpg' % i))
		photo = photo.resize((750, 500))
		photo = photo.transpose(Image.ROTATE_270)
		image.paste(photo, positions[i - 1])
		
		del photo
		
	font = ImageFont.truetype("fonts/arial.ttf", 50)
	d = ImageDraw.Draw(image)
	size = d.textsize('www.snappycampers.co.uk', font)
	
	text = Image.new('RGBA', size, (255, 255, 255, 255))
	dt = ImageDraw.Draw(text)
	dt.text((0, 0), 'www.snappycampers.co.uk', (0, 0, 0), font)
	text = text.transpose(Image.ROTATE_270)
	
	image.paste(text, (10, 1800 / 2 - size[0] / 2))
	
	del d
	del dt
	
	today = datetime.datetime.today()
	path = os.path.join(TMP_FOLDER,'results')
	if not os.path.exists(path):
		os.mkdir(path)
	filename = os.path.join(path, 'result_%s_%s.jpg' %
				(today.date().isoformat(), today.time().strftime('%H-%M-%S')))
	image.save(filename)
	return image.resize((350, 525)).transpose(Image.ROTATE_90)
			
def capture_photo(number):
	if not WIN32:
		camera.trigger_capture()
		
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

def next_screen():
	global current_screen
	current_screen += 1

TAKE_PHOTO = 4
photo_count = 1
thread_take_photo = None
thread_create_photo = None

delayScreen = SETTINGS['delay_screens']

done = False
COLLAGE = None
py_image = None

while done == False:
	for event in pygame.event.get():
		screens[current_screen].onevent(event)		
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
				#thread_create_photo = threading.Thread(target=create_photo, args=())
				#thread_create_photo.start()
				COLLAGE = create_photo()
				
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
					picture = widgets.Picture(py_image, (137, 65))
					screens[current_screen].controls.append(picture)
					py_image = None
				else:
					pygame.time.set_timer(pygame.USEREVENT + 1, 100)
					set_current_screen('WorkInProgress')

			if current_screen_is('EndScreen'):
				pygame.time.set_timer(pygame.USEREVENT + 1,
										SETTINGS['end_screen_delay'])

			if current_screen == len(screens):
				pygame.time.set_timer(pygame.USEREVENT + 1, 0)
				#thread_create_photo.join()
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
				
	screens[current_screen].render(window)
	pygame.display.flip()
	clock.tick(60)
pygame.quit()