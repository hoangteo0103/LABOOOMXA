import pygame
import Map_Window
from CONST import *
from List_Modunle import *

def Run():
	Select_Character_Screen = pygame.display.set_mode((1080, 720))
	
	Go_image = pygame.transform.scale(pygame.image.load('Game_Data/Image/Select_Character/Go_Button.png'), (200, 70))
	Background = pygame.transform.scale(pygame.image.load('Game_Data/Image/Select_Character/Background.jpg'), (1080, 720))

	Running = True 
	text = font_character.render('select character' , True, White)

	Go_Button = Button(440, 630, Go_image, 1)

	while Running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				Running = False

		Select_Character_Screen.blit(Background, (0, 0))
		Select_Character_Screen.blit(text, (330, 20))
		Go_Button.draw(Select_Character_Screen)

		if(Go_Button.isClicked(Select_Character_Screen)):
			Running = False
			Map_Window.Run()

		pygame.display.update()

