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
import subprocess
import threading, thread
import datetime
import camera

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

#vkey = VirtualKeyboard(screen)
#input_text = vkey.run()

def create_photo():
	filepattern = os.path.join(TMP_FOLDER, 'capt%04n.jpg')
	camera.get_all_files()
	thread.start_new_thread(camera.delete_all_files, ())
	
	F4x6 = (4 * 300, 6 * 300)
	image = Image.new('RGB', F4x6, (255, 255, 255))
	positions = [(100, 120), (100, 120 + 750 + 60), (100 + 60 + 500, 120), (100 + 60 + 500, 120 + 750 + 60)]
	for i in xrange(1, 5):
		photo = Image.open(os.path.join(TMP_FOLDER, 'capt000%d.jpg' % i))
		photo = photo.resize((750, 500))
		photo = photo.transpose(Image.ROTATE_270)
		image.paste(photo, positions[i])
		
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

TAKE_PHOTO = 4
photo_count = 1
thread_take_photo = None
thread_create_photo = None

done = False
while done == False:
	for event in pygame.event.get():
		screens[current_screen].onevent(event)		
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_ESCAPE:
				done = True
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.MOUSEBUTTONUP and current_screen == 0:
			##current_screen = 1
			##pygame.time.set_timer(pygame.USEREVENT + 1, 1000)
			pass			
		if event.type == pygame.USEREVENT + 1:
			current_screen += 1
			
			if current_screen == len(screens) - 3:
				pygame.time.set_timer(pygame.USEREVENT + 1, 1000)
			
			if current_screen == len(screens) - 2 and photo_count < TAKE_PHOTO:
				if thread_take_photo != None:
					pygame.time.set_timer(pygame.USEREVENT + 1, 0)
					thread_take_photo.join()
				t = threading.Thread(target=capture_photo, args=(photo_count, ))
				thread_take_photo = t
				t.start()
				photo_count += 1
				if photo_count <= TAKE_PHOTO:
					current_screen = 1
					pygame.time.set_timer(pygame.USEREVENT + 1, 1000)
					
			if current_screen == len(screens) - 2:
				pygame.time.set_timer(pygame.USEREVENT + 1, 0)
				if thread_take_photo != None:
					thread_take_photo.join()
				#thread_create_photo = threading.Thread(target=create_photo, args=())
				#thread_create_photo.start()
				collage = create_photo()
				
				mode = collage.mode
				size = collage.size
				data = collage.tobytes()
				py_image = pygame.image.fromstring(data, size, mode)
				
				picture = widgets.Picture(py_image, (137, 65))
				screens[current_screen].controls.append(picture)
				pygame.time.set_timer(pygame.USEREVENT + 1, 5000)
					
			if current_screen == len(screens) - 1:
				pygame.time.set_timer(pygame.USEREVENT + 1, 5000)
				
			if current_screen == len(screens):
				pygame.time.set_timer(pygame.USEREVENT + 1, 0)
				#thread_create_photo.join()
				current_screen = 0
				
		if event.type == widgets.Button.EVENT_BUTTONCLICK:
			if event.name == 'btnStartClick':
				if not WIN32:
					camera.check_and_close_gvfs_gphoto()
				current_screen = 1
				pygame.time.set_timer(pygame.USEREVENT + 1, 1000)
				photo_count = 0
				thread_take_photo = None
				
	screens[current_screen].render(window)

	#if input_text == 'quit':
	#	done = True
	pygame.display.flip()
	clock.tick(60)
pygame.quit()