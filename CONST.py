import pygame

Main_Menu_Window_Width = 800
Main_Menu_Window_Height = 600

Main_Menu_Image = pygame.image.load('Game_Data/Image/Main_Menu_Background.jpg')
Main_Menu_Image = pygame.transform.scale(Main_Menu_Image , (Main_Menu_Window_Width , Main_Menu_Window_Height))
Start_Button_Image = pygame.image.load('Game_Data/Image/Start_Button_Image.png')
Option_Button_Image = pygame.image.load('Game_Data/Image/Option_Button_Image.png')
Exit_Button_Image = pygame.image.load('Game_Data/Image/Exit_Button_Image.png')


#Main_Menu_Spirite = spritesheet.SpriteSheet(Main_Menu_Image)