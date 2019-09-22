import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("tower game (Pyweek28) ...")

blackTexture = pygame.image.load("./assets/back_texture.png")
room1bg = pygame.image.load("./assets/room1.png")
titlePic = pygame.image.load("./assets/title.png")
playerPic = pygame.image.load("./assets/player.png")
frontground =pygame.image.load("./assets/frontground.png")
death =pygame.image.load("./assets/death.png")

#screen.blit(pygame.transform.scale(blackTexture, (800, 400)), (0, 400))

def stillScene(picture,x,y):
	done = False

	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			elif event.type == pygame.KEYDOWN: 
				if event.key == pygame.K_SPACE:
					done = True

			
			screen.blit(picture,(x,y))
			


			pygame.display.flip()


def displayText(surface,message,x,y,size,r,g,b):
	myfont = pygame.font.Font(None,size)
	textImage = myfont.render(message, True, (r,g,b))
	surface.blit(textImage,(x,y))


class room():
	"""docstring for room"""
	def __init__(self, image,parachute,xlimit1,xlimit2,ylimit1,ylimit2):
		self.image = image
		self.parachute = parachute
		self.xlimit1 = xlimit1
		self.xlimit2 =xlimit2
		self.ylimit1 = ylimit1
		self.ylimit2 = ylimit2
	def draw(self,screen):
		screen.blit(self.image,(0,0))
	def sendLimit(self):
		return(self.xlimit1,self.xlimit2,self.ylimit1,self.ylimit2)

class player():
	"""docstring for player"""
	def __init__(self, image,x,y,limits):
		self.image = image
		self.x = x
		self.y = y
		self.limits = limits
	def move(self):
		pressed = pygame.key.get_pressed()	
		if pressed[pygame.K_UP]: self.y -=10
		elif pressed[pygame.K_DOWN]: self.y +=10
		elif pressed[pygame.K_LEFT]: self.x -= 10
		elif pressed[pygame.K_RIGHT]: self.x += 10		
		if self.y <-self.limits[2]:
			self.y = self.limits[2]
		elif self.y>self.limits[3]:
			self.y = self.limits[3]
		elif self.x < self.limits[0]:
			print("exit")
			quit()
			
		elif self.x > self.limits[1]:
			print("jump")
			quit()
			
		return(self.x,self.y)
	def draw(self,surface):
		surface.blit(self.image,(self.x,self.y))
		
		

#pregame game
done = False

screen.fill((255,255,255))
stillScene(titlePic,0,0)



#clock here--------------------------
clock = pygame.time.Clock()
counter, text = 30, '30'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
#-----

room1 = room(room1bg,False,-80,800,100,310)


jump = False
exit = False

bob = player(playerPic,50,50,(-80,800,100,310))
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()
		elif event.type == pygame.KEYDOWN: 
			if event.key == pygame.K_SPACE:
				done = True
		if event.type == pygame.USEREVENT:
			counter -= 1
			text = str(counter).rjust(3) if counter > 0 else 'boom!'



	coords_of_bob = bob.move() #and move bob of course!

	room1.draw(screen)
	screen.blit(pygame.transform.scale(blackTexture, (800,600)),(0,0))

	bob.draw(screen)

	screen.blit(frontground,(0,0))
	
	displayText(screen,"poooo",0,0,60,50,255,255)
	displayText(screen,str(counter),500,0,60,255,0,0)

	print(coords_of_bob[0],coords_of_bob[1])
	pygame.display.flip()
	clock.tick(60)