import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("tower game (Pyweek28) ...")

done = False
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()
		elif event.type == pygame.KEYDOWN: 
			if event.key == pygame.K_SPACE:
				done = True

		screen.fill((0,0,0))
		pygame.display.flip()

