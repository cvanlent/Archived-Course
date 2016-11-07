#How can we end the game without a hard kill?

#required 
import pygame
pygame.init();

#create a surface
gameDisplay = pygame.display.set_mode((800,600)) #initialize with a tuple

#lets add a title, aka "caption"
pygame.display.set_caption("Events")

pygame.display.update()		#only updates portion specified


gameExit = False
while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True




#required
pygame.quit()
quit()				#exits python