from List_Modunle import *
import Main_Menu_Window

pygame.init()
Setting_Screen = pygame.display.set_mode((Setting_Window_Width , Setting_Window_Height))

def Run():
	running = True
	while running:
		Setting_Screen.fill((120 , 120 , 120))
		# Setting_Screen.blit(Setting_Window_Background , (0 , 0))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
				Main_Menu_Window.Run()
				exit()

		pygame.display.flip()


