import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("tower game (Pyweek28) ...")

blackTexture = pygame.image.load("./assets/back_texture.png")

gameBg1 = pygame.image.load("./assets/pregame.png")
titlePic = pygame.image.load("./assets/title.png")
player = pygame.image.load("./assets/player.png")
frontground =pygame.image.load("./assets/frontground.png")

#clock here--------------------------
clock = pygame.time.Clock()
counter, text = 66, '66'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
#-----
#clock.tick(60)
#screen.blit(pygame.transform.scale(blackTexture, (800, 400)), (0, 400))

def stillScene(picture):
	done = False

	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			elif event.type == pygame.KEYDOWN: 
				if event.key == pygame.K_SPACE:
					done = True

			
			screen.blit(picture,(0,0))
			


			pygame.display.flip()



#pregame game
done = False
playerX = 50
playerY = 50

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()
		elif event.type == pygame.KEYDOWN: 
			if event.key == pygame.K_SPACE:
				done = True

	pressed = pygame.key.get_pressed()	
	if pressed[pygame.K_UP]: playerY -=10
	elif pressed[pygame.K_DOWN]: playerY +=10
	elif pressed[pygame.K_LEFT]: playerX -= 10
	elif pressed[pygame.K_RIGHT]: playerX += 10

	if playerY <-100:
		playerY = -100
	elif playerY>310:
		playerY = 310

	screen.blit(gameBg1,(0,0))
	screen.blit(pygame.transform.scale(blackTexture, (800,600)),(0,0))
	screen.blit(player,(playerX,playerY))
	screen.blit(frontground,(0,0))

	print(playerX,playerY)
	pygame.display.flip()