import pygame
import spritesheet

pygame.init()
# Screen Const
Main_Menu_Window_Width = 800
Main_Menu_Window_Height = 720
Setting_Window_Width = 1080
Setting_Window_Height = 720
Game_Window_Width = 1080
Game_Window_Height = 720
#Const Font 
font_player = pygame.font.Font('Game_Data/Font/font2.ttf', 25)
font_item = pygame.font.Font('Game_Data/Font/font5.ttf', 25)
font_quit = pygame.font.Font('Game_Data/Font/font5.ttf', 45)



# Color Const 
Black = (0,0,0) 
White = (255,255,255)
Green = (124 , 252 , 0 )


# Image
Main_Menu_Image = pygame.image.load('Game_Data/Image/Main_Menu_Background.jpg')
Main_Menu_Image = pygame.transform.scale(Main_Menu_Image , (Main_Menu_Window_Width , Main_Menu_Window_Height))
Play_Button_Image = pygame.image.load('Game_Data/Image/Play_Button_Image.png')
Setting_Button_Image = pygame.image.load('Game_Data/Image/Setting_Button_Image.png')
Instruction_Button_Image = pygame.image.load('Game_Data/Image/Instruction_Button_Image.png')
Quit_Button_Image = pygame.image.load('Game_Data/Image/Quit_Button_Image.png')
Skin_Image = [pygame.image.load(f'Game_Data/Image/Skin_{i}.png') for i in range(1,8)]
Item_Frame = [pygame.image.load(f'Game_Data/Image/Item/Item_{i}.png') for i in range(1, 7)]
Number_Item_Frame = [4 , 8 , 6 ,7 , 4, 22]
Item_Frame_Size = [(1024 ,1024) , (16 ,16) , (250 ,250) , (220 , 93), (500, 500), (192, 192)]


Num_Idle_Frames = [4 , 4 , 4 , 4 , 9 , 18 , 9 ]
Num_Move_Frames = [10 , 10 , 10 , 10 , 22 , 42 , 17]

Heigh_Frames = [24 , 24 , 24 , 24 , 80 ,  80 , 64]
Width_Frames = [24 , 24 , 24 , 24 , 120 , 80 , 64 ]

#Profile 
Skin_SpriteSheet = [spritesheet.SpriteSheet(Skin_Image[i]) for i in range(7)]
Skin_Profile_Image = [pygame.transform.scale(Skin_SpriteSheet[i].get_image(0 , Width_Frames[i] , Heigh_Frames[i] , 1 , Black) , (150 ,140) ) for i in range(7)]


Profile_Image = pygame.transform.scale(pygame.image.load('Game_Data/Image/Player_Profile/Profile.png') , (264 , 180) )
Size_Item_Profile = 25
Heart_Image = pygame.transform.scale(pygame.image.load('Game_Data/Image/Item/heart.png') , (40 , 40) )  
Potion_Image = pygame.transform.scale(pygame.image.load('Game_Data/Image/Item/potion.png') , (Size_Item_Profile , Size_Item_Profile) )
Speed_Image = pygame.transform.scale(pygame.image.load('Game_Data/Image/Item/speed.png') , (Size_Item_Profile , Size_Item_Profile) )
Bomb_Image = pygame.transform.scale(pygame.image.load('Game_Data/Image/Item/bomb.png') , (Size_Item_Profile , Size_Item_Profile) )



bomb_frames = [pygame.transform.scale(pygame.image.load(f'Game_Data/Image/bombs/tile0{i}.png') , (48 , 48 ) ) for i in range(0,12)]
num_explosions_frames = 12
left_explosion = [pygame.transform.scale(pygame.image.load(f'Game_Data/Image/explosions/test-{i}.png') , (48 , 48 ) ) for i in range(0,12)]
right_explosion = [pygame.transform.flip(left_explosion[i], True, False) for i in range(0,num_explosions_frames)]
up_explosion = [pygame.transform.rotate(left_explosion[i] , 270) for i in range(0 , num_explosions_frames)]
down_explosion = [pygame.transform.rotate(left_explosion[i] , 90) for i in range(0 , num_explosions_frames)]
explosion_frames = [left_explosion , right_explosion , up_explosion , down_explosion ]
storm_frames = [pygame.transform.scale(pygame.image.load(f"Game_Data/Image/storm/storm-{i}.png") , (48 ,48)) for i in range(0,30)]
boss_frames = [pygame.transform.scale(pygame.image.load(f"Game_Data/Image/test/test-{i}.png") , (144 ,144)) for i in range(0,52)]

portal_frames = [pygame.transform.scale(pygame.image.load(f"Game_Data/Image/portal/portal-{i}.png") , (48 ,48)) for i in range(0,9)]


bubble_image = pygame.transform.scale(pygame.image.load("Game_Data/Image/Item/bubble.png"), (48, 48))
bubble_image.set_colorkey((100, 100,100))

bomb_image = pygame.transform.scale(pygame.image.load('Game_Data/Image/Bomb_Image.png') , (48 , 48)) 

# Cell Const
Cell_Width = 48
Cell_Height = 48

# Key Const
Player_Key = []
Player_Key.append([15 , 10 , 13 , 32 , 28])
Player_Key.append([40 , 45 , 46 , 47 , 48])
Player_Key.append([1 , 2 , 3 , 4 , 5])
Player_Key.append([42 , 19 , 21 , 18 , 20])

Key_Image_Scale = 4
Empty_Key_Image = pygame.image.load('Game_Data/Image/Setting_Image/button.png')
Empty_Key_Image = pygame.transform.scale(Empty_Key_Image , (int(Empty_Key_Image.get_width() * Key_Image_Scale) , int(Empty_Key_Image.get_height() * Key_Image_Scale)))
Key_List = []
Key_Image = []
Key_Pos = [10 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 23 , 41 , 38 , 25 , 14 , 26 , 27 , 28 , 19 , 29 , 30 , 31 , 43 , 42 , 20 , 21 , 12 , 15 , 24 , 16 , 18 , 40 , 13 , 37 , 17 , 36 , 35 , 44 , 11 , 34 , 45 , 22 , 32 , 39 , 0 , 46 , 48 , 33 , 47]
for i in range(10):
	Key_List.append(pygame.key.key_code(str(i)))
	Image = pygame.image.load(f'Game_Data/Image/Setting_Image/key_{i}.png')
	width = Image.get_width()
	height = Image.get_height() 
	Image = pygame.transform.scale(Image , (int(width * Key_Image_Scale) , int(height * Key_Image_Scale)))
	Key_Image.append(Image)
for i in range(97 , 123):
	Key_List.append(pygame.key.key_code(chr(i)))
	Image = pygame.image.load(f'Game_Data/Image/Setting_Image/key_{chr(i)}.png')
	width = Image.get_width()
	height = Image.get_height() 
	Image = pygame.transform.scale(Image , (int(width * Key_Image_Scale) , int(height * Key_Image_Scale)))
	Key_Image.append(Image)
for i in ('left alt' , 'right alt' , 'capslock' , 'left ctrl' , 'right ctrl' , 'left shift' , 'right shift' , 'space' , 'tab' , 'left' , 'right' , 'up' , 'down'):
	Key_List.append(pygame.key.key_code(i))
	Image = pygame.image.load(f'Game_Data/Image/Setting_Image/key_{i}.png')
	width = Image.get_width()
	height = Image.get_height() 
	Image = pygame.transform.scale(Image , (int(width * Key_Image_Scale) , int(height * Key_Image_Scale)))
	Key_Image.append(Image)