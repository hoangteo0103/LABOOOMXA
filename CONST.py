import pygame
import spritesheet

Main_Menu_Window_Width = 800
Main_Menu_Window_Height = 600

Main_Menu_Image = pygame.image.load('Game_Data/Image/Main_Menu_Background.jpg')
Main_Menu_Button_Image = pygame.image.load('Game_Data/Image/MainMenu_Button.jpg')
Main_Menu_sprite_sheet = spritesheet.SpriteSheet(Main_Menu_Button_Image)
Black = (0 ,0 ,0)
Start_Button_Image = Main_Menu_sprite_sheet.get_image(1 , 100 , 100 , 1,Black)


#Main_Menu_Spirite = spritesheet.SpriteSheet(Main_Menu_Image)