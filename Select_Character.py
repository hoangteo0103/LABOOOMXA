import pygame
import Map_Window
import Main_Menu_Window
from CONST import *
from List_Modunle import *
# from Character import *

def Run():
	pygame.time.delay(300)
	Select_Character_Screen = pygame.display.set_mode((1080, 720))
	
	Go_image = pygame.transform.scale(pygame.image.load('Game_Data/Image/Select_Character/Go_Button.png'), (200, 70))
	Background = pygame.transform.scale(pygame.image.load('Game_Data/Image/Select_Character/Background.jpg'), (1080, 720))

	Running = True 
	text = font_character.render('select character' , True, White)

	Go_Button = Button(440, 630, Go_image, 1)

	while Running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				Main_Menu_Window.Run()
				Running = False
				exit()

		Select_Character_Screen.blit(Background, (0, 0))
		Select_Character_Screen.blit(text, (330, 10))
		Go_Button.draw(Select_Character_Screen)

		for i in range (0 , 4):
			Character_List[i].draw(Select_Character_Screen)

		if(Go_Button.isClicked(Select_Character_Screen)):
			Running = False
			Map_Window.Run()

		pygame.display.update()

