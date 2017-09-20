import pygame
from virtualKeyboard import VirtualKeyboard
import screen

WELCOME_SCREEN = [{
"background":[139,174,233],
"labels":[
	{
		"position":[20, 100],
		"text":"Welcome to Snappy Campers",
		"color":[0, 0, 0],
		"font":"Arial",
		"font_size":85
	},
	{
		"position":[20, 350],
		"text":"Please Touch Screen to Start",
		"color":[0, 0, 0],
		"font":"Arial",
		"font_size":85
	}]
},
{
"background":[139,174,233],
"labels":[
	{
		"position":[400, 50],
		"text":"5",
		"color":[0, 0, 0],
		"font":"Arial",
		"font_size":385
	}]
}]

pygame.init()
#pygame.mouse.set_visible(0)
welcome = screen.Screen(WELCOME_SCREEN[1])
s5 = 0;
screen = pygame.display.set_mode((1024, 600), pygame.HWSURFACE, 32)

done = False
clock = pygame.time.Clock()

#vkey = VirtualKeyboard(screen)
#input_text = vkey.run()

while done == False:
	for event in pygame.event.get():
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_ESCAPE:
				done = True

	welcome.render(screen)

	#if input_text == 'quit':
	#	done = True
	pygame.display.flip()
	clock.tick(60)
pygame.quit()