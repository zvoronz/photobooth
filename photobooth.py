import pygame
from virtualKeyboard import VirtualKeyboard
import widgets

WELCOME_SCREEN = [{
"background":[139,174,233],
"labels":[
	{
		"position":[0, 100],
		"text":"Welcome to Snappy Campers",
		"color":[0, 0, 0],
		"font":"Arial",
		"font_size":70,
		"hvaligment":[True, False]
	},
	{
		"position":[0, 350],
		"text":"Please Touch Screen to Start",
		"color":[0, 0, 0],
		"font":"Arial",
		"font_size":70,
		"hvaligment":[True, False]
	}]
},
{
"background":[139,174,233],
"labels":[
	{
		"position":[100, 50],
		"text":"5",
		"color":[0, 0, 0],
		"font":"Arial",
		"font_size":385,
		"hvaligment":[True, True]
	}]
},
{
"background":[139,174,233],
"labels":[
	{
		"position":[100, 50],
		"text":"4",
		"color":[0, 0, 0],
		"font":"Arial",
		"font_size":385,
		"hvaligment":[True, True]
	}]
},
{
"background":[139,174,233],
"labels":[
	{
		"position":[100, 50],
		"text":"3",
		"color":[0, 0, 0],
		"font":"Arial",
		"font_size":385,
		"hvaligment":[True, True]
	}]
},
{
"background":[139,174,233],
"labels":[
	{
		"position":[100, 50],
		"text":"2",
		"color":[0, 0, 0],
		"font":"Arial",
		"font_size":385,
		"hvaligment":[True, True]
	}]
},
{
"background":[139,174,233],
"labels":[
	{
		"position":[100, 50],
		"text":"1",
		"color":[0, 0, 0],
		"font":"Arial",
		"font_size":385,
		"hvaligment":[True, True]
	}]
},
{
"background":[139,174,233],
"labels":[
	{
		"position":[100, 50],
		"text":"0",
		"color":[0, 0, 0],
		"font":"Arial",
		"font_size":385,
		"hvaligment":[True, True]
	}]
},
{
"background":[139,174,233],
"labels":[
	{
		"position":[0, 20],
		"text":"Thank You",
		"color":[0, 0, 0],
		"font":"Arial",
		"font_size":95,
		"hvaligment":[True, False]
	},
	{
		"position":[0, 175],
		"text":"Please Take Photo Below",
		"color":[0, 0, 0],
		"font":"Arial",
		"font_size":85,
		"hvaligment":[True, False]
	},
	{
		"position":[100, 400],
		"text":"www.snappycampers.co.uk",
		"color":[0, 0, 0],
		"font":"Arial",
		"font_size":65,
		"hvaligment":[True, False]
	}]
}]

pygame.init()
#pygame.mouse.set_visible(0)

screens = []
current_screen = 0
for item in WELCOME_SCREEN:
	screens.append(widgets.Screen(item))
	
window = pygame.display.set_mode((1024, 600), pygame.HWSURFACE, 32)

done = False
clock = pygame.time.Clock()

#vkey = VirtualKeyboard(screen)
#input_text = vkey.run()

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
			if current_screen == len(screens):
				pygame.time.set_timer(pygame.USEREVENT + 1, 10000)
				current_screen = 0

	screens[current_screen].render(window)

	#if input_text == 'quit':
	#	done = True
	pygame.display.flip()
	clock.tick(60)
pygame.quit()