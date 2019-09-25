import pygame
from fadetoWhite import *
from random import randrange
pygame.mixer.pre_init()
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
player_fall= pygame.image.load("./assets/player_fall.png")

frontground =pygame.image.load("./assets/frontground.png")
death =pygame.image.load("./assets/death.png")
parachute =pygame.image.load("./assets/parachute.png")

#scene
splash =pygame.image.load("./assets/splash.png")
scene1 =pygame.image.load("./assets/scene1.png")
scene2 =pygame.image.load("./assets/scene2.png")
scene3 =pygame.image.load("./assets/scene3.png")


#game object
building = pygame.image.load("./assets/building.png")
cloud = pygame.image.load("./assets/cloud.png")
city = pygame.image.load("./assets/city.png")
explosion1 = pygame.image.load("./assets/explosion1.png")
explosion2 = pygame.image.load("./assets/explosion2.png")
bird = pygame.image.load("./assets/bird.png")



#game cg
death1 =pygame.image.load("./assets/death1.png")

def stillScene(picture,x,y,button):
	done = False

	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			elif event.type == pygame.KEYDOWN: 
				if event.key == button:
					done = True

			
			screen.blit(pygame.transform.scale(picture,(800,600)),(x,y))
			


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
				if event.key == pygame.K_RETURN:
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
		# print(PX,PY)
		clock.tick(60)








#pregame	
def pregame():
	pygame.mixer.music.load("./assets/falling.ogg")
	#pygame.mixer.music.load("./assets/title.ogg")  
	pygame.mixer.music.play(-1,0.0)
	stillScene(titlePic,0,0,pygame.K_SPACE)
	make_room(room1bg,300,100)
	make_room(room2bg,500,300)
	make_room(room3bg,500,150)
	stillScene(parachute,0,0,pygame.K_SPACE)

	make_room(room1bg,300,100)
	stillScene(scene1,0,0,pygame.K_SPACE)
	stillScene(scene2,0,0,pygame.K_SPACE)
	#stillScene(scene3,0,0,pygame.K_j)


def fall_animation():
	done = False
	start_fall = False
	#fall variables
	y = 0
	x = 0
	xv = 10
	yv = 3
	gravity = 0.5

	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			elif event.type == pygame.KEYDOWN: 
				if event.key == pygame.K_j:
					start_fall = True
		screen.blit(scene3,(0,0))




		screen.blit(player_fall,(x,y))
		if start_fall == True:
			y+=yv
			x+=xv
			yv+=gravity

		if y>= 800:
			done = True
		pygame.display.flip()

# class falling_object():
# 	"""docstring for falling_object"""
# 	def __init__(self, x, y, speed):
# 		self.x = x
# 		self.y = y
# 		self.speed = speed
# 	def move(self,loop):
# 		done = False
# 		while not done:
# 			self.y-=self.speed
# 			if loop == True:
# 				if self.y<= -600:
# 					self.y = 0
# 			print(self.y)
# 	def draw(self,image):
# 		# screen.blit(image,(self.x,self.y))
# 		screen.blit(building,(0,0))


class bird():
	"""docstring for ClassName"""
	def __init__(self, x,y,image):
		self.x = x
		self.y = y
	def move(self):
		self.x = randrange(186,720)
		self.y = 600
		self.y-=1
	def draw(self,surface):
		surface.blit(image,(self.x,self.y))

						

def falling_game():
	
	done = False

	#fall variables
	meters_fallen = 0
	playerX = 400
	playerY = 10
	player_image = player_fall

	buildingY = 0
	cloudY = 300
	cityY = 600



	#bird
	bird_number = randrange(0,2)
	birdY = 0
	birdX = randrange(186,720)

	#fall objects
	# building_o = falling_object(0,0,5)


	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()


		pressed = pygame.key.get_pressed()	
		if pressed[pygame.K_LEFT]: playerX -= 10
		elif pressed[pygame.K_RIGHT]: playerX += 10
		elif pressed[pygame.K_UP]: playerY -= 10
		elif pressed[pygame.K_DOWN]: playerY += 10

		if playerX<=0:
			playerX = 0
		elif playerX>=720:
			playerX=720
		elif playerY<=0:
			playerY= 0
		elif playerY>=520:
			playerY=520
			


		screen.fill((113, 197, 255))
		#screen.blit(scene3,(0,0))
		# building_o.move(True)
		
		#background moving
		screen.blit(city,(0,cityY))
		screen.blit(cloud,(200,cloudY))
		screen.blit(building,(0,buildingY))



		screen.blit(player_image,(playerX,playerY))
		# building_o.draw(building)


		#background change y
		buildingY-=10
		cloudY-=0.1
		cityY-=0.2
		if buildingY <=-600:
			buildingY=0
		if cityY <=297:
			print("you done")
		if playerX<=186:

			return "dead"


			# player_image = explosion1


		pygame.display.flip()






# #title
# stillScene(splash,0,0,pygame.K_SPACE)	
# pregame()
# fall_animation()

if falling_game() == "dead":
	pygame.mixer.music.stop()
	pygame.mixer.music.load("./assets/truly_unfortunate.ogg")
	pygame.mixer.music.play(-1,0.0)
	fadetoWhite(screen,death1)
	stillScene(death,0,0,pygame.K_SPACE)



