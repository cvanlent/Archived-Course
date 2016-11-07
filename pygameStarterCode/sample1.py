#required 
import pygame
pygame.init();

#create a surface
gameDisplay = pygame.display.set_mode((800,600)) #initialize with a tuple

#lets add a title, aka "caption"
pygame.display.set_caption("Events")

#pygame.display.flip() 		#similar to a flip book, updates entire surface
pygame.display.update()		#only updates portion specified


gameExit = False
while not gameExit:
	for event in pygame.event.get():
		print(event)



#required
pygame.quit()
quit()				#exits python