from List_Modunle import *
import Main_Menu_Window
from Play_Board import *

def Run():
	Setting_Screen = pygame.display.set_mode((Setting_Window_Width , Setting_Window_Height))
	Setting_Screen.fill((120 , 120 , 120))

	Key_Button = []
	x = 0
	y = 0
	for i in Key_Image:
		Key_Button.append(Button(x * 100 , y * 40 , i , 3))
		x += 1
		if x * 100 > 1000:
			x = 0
			y += 1

	running = True
	while running:
		# Setting_Screen.blit(Setting_Window_Background , (0 , 0))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
				Main_Menu_Window.Run()
				exit()
		for i in Key_Button:
			i.draw(Setting_Screen)

		pygame.display.update()


