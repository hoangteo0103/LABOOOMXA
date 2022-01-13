import pygame
from CONST import *
from List_Modunle import *
import Main_Menu_Window

Quit_Screen = pygame.display.set_mode((800, 720))

def Quit_Window() :
	Run = True 
	text = font_quit.render("Do you want to quit the game ?", True, White)
	Yes_Image = pygame.transform.scale(pygame.image.load('Game_Data/Image/Quit_Image/Yes_Button.png'), (200, 60))
	No_Image = pygame.transform.scale(pygame.image.load('Game_Data/Image/Quit_Image/No_Button.png'), (200, 60))
	Quit_Image = pygame.transform.scale(pygame.image.load('Game_Data/Image/Quit_Image/Quit_Image.jpg'), (800, 720))


	Yes_Button = Button(120, 350, Yes_Image, 1)
	No_Button = Button(465, 350, No_Image, 1)

	while Run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				Run = False
				exit()

		Quit_Screen.blit(Quit_Image, (0, 0))
		Quit_Screen.blit(text, (60, 100))
		
		Yes_Button.draw(Quit_Screen)
		No_Button.draw(Quit_Screen)

		Yes_val = Yes_Button.isClicked(Quit_Screen)
		if Yes_val == 1:
			exit()

		No_val = No_Button.isClicked(Quit_Screen)
		if(No_val == 1):
			Main_Menu_Window.Run()
			exit()

		pygame.display.update()
