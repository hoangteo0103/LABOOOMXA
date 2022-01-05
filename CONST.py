import pygame
import spritesheet

# Screen Const
Main_Menu_Window_Width = 800
Main_Menu_Window_Height = 720
Setting_Window_Width = 1080
Setting_Window_Height = 720
Game_Window_Width = 1080
Game_Window_Height = 720

# Color Const 
Black = (0,0,0) 


# Image
Main_Menu_Image = pygame.image.load('Game_Data/Image/Main_Menu_Background.jpg')
Main_Menu_Image = pygame.transform.scale(Main_Menu_Image , (Main_Menu_Window_Width , Main_Menu_Window_Height))
Play_Button_Image = pygame.image.load('Game_Data/Image/Play_Button_Image.png')
Setting_Button_Image = pygame.image.load('Game_Data/Image/Setting_Button_Image.png')
Instruction_Button_Image = pygame.image.load('Game_Data/Image/Instruction_Button_Image.png')
Quit_Button_Image = pygame.image.load('Game_Data/Image/Quit_Button_Image.png')
Skin_Image = [pygame.image.load(f'Game_Data/Image/Skin_{i}.png') for i in range(1,5)]

# Cell Const
Cell_Width = 48
Cell_Height = 48
