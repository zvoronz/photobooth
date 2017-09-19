import pygame

pygame.init()
pygame.mouse.set_visible(0)
screen = pygame.display.set_mode((640, 480), pygame.HWSURFACE, 32)

done = False
clock = pygame.time.Clock()

BLUE = (0, 0, 255)
YELLOW = (0, 255, 255)

font = pygame.font.Font(None, 75)
text = font.render('Photobooth', True, YELLOW)

while done == False:
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONUP:
			done = True

	screen.fill(BLUE)
	screen.blit(text, (180, 50))

	pygame.display.flip()
	clock.tick(60)
pygame.quit()