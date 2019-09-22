import pygame
import os
pygame.init()
def messageText(text,x,y,size,surface,red,green,blue):

	myFont = pygame.font.SysFont('Consolas', size)

	label = myFont.render(text, 1, (red, green, blue))

	surface.blit(label, (x, y))

	pygame.display.flip()

 #how to use
 #messageText("Text to display",x,y,size,what surface,redlevel,greenlevel,bluelevel)
