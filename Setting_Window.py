from List_Modunle import *

pygame.init()
Setting_Screen = pygame.display.set_mode((Setting_Window_Width , Setting_Window_Height))

def Run():
	Run = True
	while Run:
		Setting_Screen.fill((120 , 120 , 120))
		# Setting_Screen.blit(Setting_Window_Background , (0 , 0))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				Run = False

		pygame.display.flip()


