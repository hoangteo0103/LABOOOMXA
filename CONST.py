import pygame
import spritesheet

# Screen Const
Main_Menu_Window_Width = 800
Main_Menu_Window_Height = 720
Setting_Window_Width = 800
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
bomb_frames = [pygame.transform.scale(pygame.image.load(f'Game_Data/Image/bombs/tile0{i}.png') , (48 , 48 ) ) for i in range(0,12)]
left_explosion = [pygame.transform.scale(pygame.image.load(f'Game_Data/Image/explosions/img_{i}.png') , (48 , 48 ) ) for i in range(0,40)]
right_explosion = [pygame.transform.flip(left_explosion[i], True, False) for i in range(0,40)]
up_explosion = [pygame.transform.rotate(left_explosion[i] , 270) for i in range(0 , 40)]
down_explosion = [pygame.transform.rotate(left_explosion[i] , 90) for i in range(0 , 40)]
explosion_frames = [left_explosion , right_explosion , up_explosion , down_explosion ]

bomb_image = pygame.transform.scale(pygame.image.load('Game_Data/Image/Bomb_Image.png') , (48 , 48)) 
bomb_image.set_colorkey((100, 100,100))
# Cell Const
Cell_Width = 48
Cell_Height = 48