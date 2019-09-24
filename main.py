import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("tower game (Pyweek28) ...")

blackTexture = pygame.image.load("./assets/back_texture.png")
room1bg = pygame.image.load("./assets/room1.png")
room2bg = pygame.image.load("./assets/room2.png")
room3bg = pygame.image.load("./assets/room3.png")
titlePic = pygame.image.load("./assets/title.png")
playerR = pygame.image.load("./assets/player_right.png")
playerL= pygame.image.load("./assets/player_left.png")

frontground =pygame.image.load("./assets/frontground.png")
death =pygame.image.load("./assets/death.png")



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








class player():
	"""docstring for player"""
	def __init__(self,x,y,limits,left,room_number):
		self.x = x
		self.y = y
		self.limits = limits
		self.left = left
		self.room_number = room_number
	def move(self):
		self.room_number = 1
		left_exit = False
		right_exit = False
		has_parachute = False
		pressed = pygame.key.get_pressed()	
		# if pressed[pygame.K_UP]: self.y -=10
		# elif pressed[pygame.K_DOWN]: self.y +=10
		if pressed[pygame.K_LEFT]: 
			self.x -= 10
			self.left = True
		elif pressed[pygame.K_RIGHT]:
			self.x += 10
			self.left = False

		if self.x <= self.limits[0]: #good left
			self.x = self.limits[0]
			left_exit = True


			if self.room_number ==1 or self.room_number ==1:

				self.x = 690
				self.y = 210
				print("Lexit")

			
		elif self.x >= self.limits[1]: #right
			self.x = self.limits[1]
			right_exit = True


			if self.room_number ==3 or self.room_number ==2:
				print("Rexit")
				self.x = 30
				self.y = 210

		elif self.y <=self.limits[2]:#good top
			self.y = self.limits[2]

		elif self.y>=self.limits[3]: #goooood bottom
			self.y = self.limits[3]

	
		return(self.x,self.y,right_exit,left_exit,self.left,has_parachute,self.room_number)
	def draw(self,surface,image):
		surface.blit(image,(self.x,self.y))
		
		
def make_room(image,PX,PY):
	#pregame game
	done = False

	screen.fill((255,255,255))
	# stillScene(titlePic,0,0)



	#clock here--------------------------
	clock = pygame.time.Clock()
	counter, text = 30, '30'.rjust(3)
	pygame.time.set_timer(pygame.USEREVENT, 1000)
	#-----




	bob = player(PX,PY,(-40,760,0,316),True,1)#-------------------------------------
	coords_of_bob = bob.move() #and move bob of course!


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


		screen.blit(image,(0,0))
		#screen.blit(pygame.transform.scale(blackTexture, (800, 400)), (0, 400))
		screen.blit(pygame.transform.scale(blackTexture, (800, 600)), (0, 0))
		#rooms-------------------------------------------------------

	#return(self.x ,self.y, right_exit, left_exit ,self.left ,has_parachute, self.room_number)


		coords_of_bob = bob.move() #and move bob of course!

		# if coords_of_bob[2] == True and coords_of_bob[5] == False:#move right
		# 	if current_room == room1:
		# 		stillScene(death,0,0)

		# elif coords_of_bob[2] == True and coords_of_bob[5] == True:#move right
		# 	if current_room == room1:
		# 		quit()#START GAME!!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

		# if coords_of_bob[3] == True and current_room == room1:
		# 	current_room == room2
			










		if coords_of_bob[4] == True:#if go left
			bob.draw(screen,playerL)
		elif coords_of_bob[4] == False:#if go right
			bob.draw(screen,playerR)


		if coords_of_bob[2]: #if exit right
			done=True
			return "right"
		elif coords_of_bob[3]:
			done = True
			return "left"
		
		# displayText(screen,"poooo",0,0,60,50,255,255)
		# displayText(screen,str(counter),500,0,60,255,0,0)

		# print(coords_of_bob)
		

		pygame.display.flip()
		print(PX,PY)
		clock.tick(60)


make_room(room1bg,300,100)
make_room(room2bg,500,300)
make_room(room3bg,500,150)




