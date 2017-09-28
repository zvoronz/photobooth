import pygame
from virtualKeyboard import VirtualKeyboard
import widgets
import json
from PIL import Image, ImageDraw, ImageFont
import os

SCENES = []
with open('config.json', 'r') as f:
	SCENES = json.loads(f.read())

TMP_FOLDER = 'tmp'

pygame.init()
#pygame.mouse.set_visible(0)

screens = []
current_screen = 0
for item in SCENES:
	screens.append(widgets.Screen(item))
	
window = pygame.display.set_mode((800, 480), pygame.HWSURFACE, 32)

done = False
clock = pygame.time.Clock()

#vkey = VirtualKeyboard(screen)
#input_text = vkey.run()

def create_photo():
	F4x6 = (4 * 300, 6 * 300)
	image = Image.new('RGB', F4x6, (255, 255, 255))
	positions = [(100, 120), (100, 120 + 750 + 60), (100 + 60 + 500, 120), (100 + 60 + 500, 120 + 750 + 60)]
	for i in xrange(4):
	
		photo = Image.open(os.path.join(os.path.curdir, TMP_FOLDER, 'capt000%d.jpg' % i))
		photo = photo.resize((750, 500))
		photo = photo.transpose(Image.ROTATE_270)
		image.paste(photo, positions[i])
		
		del photo
		
	font = ImageFont.truetype("arial.ttf", 50)
	d = ImageDraw.Draw(image)
	size = d.textsize('www.snappycampers.com', font)
	
	text = Image.new('RGBA', size, (255, 255, 255, 255))
	dt = ImageDraw.Draw(text)
	dt.text((0, 0), 'www.snappycampers.com', (0, 0, 0), font)
	text = text.transpose(Image.ROTATE_270)
	
	image.paste(text, (10, 1800 / 2 - size[0] / 2))
	
	del d
	del dt
	
	image.save('my.jpg')

create_photo()

while done == False:
	for event in pygame.event.get():
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_ESCAPE:
				done = True
		if event.type == pygame.MOUSEBUTTONUP and current_screen == 0:
			current_screen = 1
			pygame.time.set_timer(pygame.USEREVENT + 1, 1000)
		if event.type == pygame.USEREVENT + 1:
			current_screen += 1
			if current_screen == len(screens) - 1:
				pygame.time.set_timer(pygame.USEREVENT + 1, 10000)
				create_photo()
			if current_screen == len(screens):
				pygame.time.set_timer(pygame.USEREVENT + 1, 0)
				current_screen = 0
				

	screens[current_screen].render(window)

	#if input_text == 'quit':
	#	done = True
	pygame.display.flip()
	clock.tick(60)
pygame.quit()
