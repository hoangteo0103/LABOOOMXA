from List_Modunle import *
import Main_Menu_Window
from Play_Board import *

def Run():
	Setting_Screen = pygame.display.set_mode((Setting_Window_Width , Setting_Window_Height))
	Setting_Screen.fill((120 , 120 , 120))

	Key_Button = []
	x = 0
	y = 480
	dis = 5
	empty_area = 10
	for j in range(49):
		for i in range(49):
			if Key_Pos[i] != j:
				continue;
			if Key_Pos[i] == 0:
				x = 35 * Key_Image_Scale + dis + empty_area
			elif Key_Pos[i] == 11:
				x = 28 * Key_Image_Scale + dis + empty_area
				y += 14 * Key_Image_Scale
			elif Key_Pos[i] == 22:
				x = 35 * Key_Image_Scale + dis + empty_area
				y += 14 * Key_Image_Scale
			elif Key_Pos[i] == 34:
				x = empty_area
				y += 14 * Key_Image_Scale
			Key_Button.append(Button(x, y , Key_Image[i] , 1))
			if Key_Pos[i] == 0:
				x += 20 * Key_Image_Scale + dis
			elif Key_Pos[i] == 11:
				x += 27 * Key_Image_Scale + dis
			elif Key_Pos[i] == 22:
				x += 20 * Key_Image_Scale + dis
			elif Key_Pos[i] == 34:
				x += 28 * Key_Image_Scale + dis
			elif Key_Pos[i] == 32:
				x += 256
			elif Key_Pos[i] == 39:
				x += 22 * Key_Image_Scale + dis
			elif Key_Pos[i] == 35:
				x += 22 * Key_Image_Scale + dis
			elif Key_Pos[i] == 43:
				x += 13 * Key_Image_Scale + dis
			elif Key_Pos[i] == 44:
				x += 22 * Key_Image_Scale + dis
			elif Key_Pos[i] == 45:
				x += 28 * Key_Image_Scale + dis + 22
			else:
				x += 12 * Key_Image_Scale + dis
	
	Player_Key_Button = [[] , [] , [] , []]
	for i in range(4):
		for j in range(5):
			Player_Key_Button[i].append(Button(i * 200 + 200 , j * Key_Image_Scale * 14 + 150 , Key_Image[Player_Key[i][j]] , 1))

	running = True
	P1 = -1
	P2 = -1
	while running:
		# Setting_Screen.blit(Setting_Window_Background , (0 , 0))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
				Main_Menu_Window.Run()
				exit()
		
		for i in range(4):
			for j in range(5):
				if Player_Key_Button[i][j].isClicked(Setting_Screen):
					P1 = i
					P2 = j
					Player_Key_Button[P1][P2] = Button(P1 * 200 + 200 , P2 * Key_Image_Scale * 14 + 150 , Empty_Key_Image , 1)

		for i in range(49):
			if Key_Button[i].isClicked(Setting_Screen):
				if P1 != -1:
					for j in range(49):
						if Key_Pos[j] != i:
							continue
						Player_Key[P1][P2] = j
						Player_Key_Button[P1][P2] = Button(P1 * 200 + 200 , P2 * Key_Image_Scale * 14 + 150 , Key_Image[j] , 1)
					P1 = -1
					P2 = -1

		Setting_Screen.fill((120 , 120 , 120))
		for i in Key_Button:
			i.draw(Setting_Screen)
		for i in range(4):
			for j in Player_Key_Button[i]:
				j.draw(Setting_Screen)

		pygame.display.update()


