from List_Modunle import *
import Main_Menu_Window
from Play_Board import *

def Run():
	Setting_Screen = pygame.display.set_mode((Setting_Window_Width , Setting_Window_Height))
	Setting_Screen.fill((120 , 120 , 120))

	Key_Button = []
	x = 0
	y = 500
	scale = 4
	dis = 5
	empty_area = 10
	for j in range(49):
		for i in range(49):
			if Key_Pos[i] != j:
				continue;
			if Key_Pos[i] == 0:
				x = 35 * scale + dis + empty_area
			elif Key_Pos[i] == 11:
				x = 28 * scale + dis + empty_area
				y += 14 * scale
			elif Key_Pos[i] == 22:
				x = 35 * scale + dis + empty_area
				y += 14 * scale
			elif Key_Pos[i] == 34:
				x = empty_area
				y += 14 * scale
			Key_Button.append(Button(x, y , Key_Image[i] , scale))
			if Key_Pos[i] == 0:
				x += 20 * scale + dis
			elif Key_Pos[i] == 11:
				x += 27 * scale + dis
			elif Key_Pos[i] == 22:
				x += 20 * scale + dis
			elif Key_Pos[i] == 34:
				x += 28 * scale + dis
			elif Key_Pos[i] == 32:
				x += 256
			elif Key_Pos[i] == 39:
				x += 22 * scale + dis
			elif Key_Pos[i] == 35:
				x += 22 * scale + dis
			elif Key_Pos[i] == 43:
				x += 13 * scale + dis
			elif Key_Pos[i] == 44:
				x += 22 * scale + dis
			elif Key_Pos[i] == 45:
				x += 28 * scale + dis + 22
			else:
				x += 12 * scale + dis

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


