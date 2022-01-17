from List_Modunle import *
from CONST import *

def cvert(Str):
	if Str == 'left alt': return 'lalt'
	if Str == 'right alt': return 'ralt'
	if Str == 'left ctrl': return 'lctrl'
	if Str == 'right ctrl': return 'rctrl'
	if Str == 'left shift': return 'lshift'
	if Str == 'right shift': return 'rshift'
	if Str == 'capslock': return 'caps'
	return Str

class Character():

	def __init__(self , Id):
		self.Id = Id
		self.x = Character_Coord[Id - 1][0]
		self.y = Character_Coord[Id - 1][1]

		self.Pos_Skin = [self.x + 50 , self.y + 45]
		self.Pos_Left = [self.x + 30 , self.y + 115]
		self.Pos_Right = [self.x + 190 , self.y + 115]
		self.Pos_Add = [self.x + 205 , self.y + 5]
		self.Pos_Del = [self.x + 205 , self.y + 5]
		self.Key_Width = 60
		self.Key_Height = 30
		self.Pos_Key = [[self.x + 240 + (self.Key_Width + 5) * 1 , self.y + 70] , [self.x + 240 + (self.Key_Width + 5) * 0 , self.y + 70 + (self.Key_Height + 10)] , [self.x + 240 + (self.Key_Width + 5) * 1 , self.y + 70 + (self.Key_Height + 10)] , [self.x + 240 + (self.Key_Width + 5) * 2 , self.y + 70 + (self.Key_Height + 10)] , [self.x + 236 + (self.Key_Width + 5) * 0 , self.y + 80 + (self.Key_Height + 10) * 2]]

		self.Skin_List = [pygame.transform.scale(Skin_SpriteSheet[i].get_image(0 , Width_Frames[i] , Heigh_Frames[i] , 1 , Black) , (140 , 160)) for i in range(7)]
		self.Cur_Skin = 0
		self.Cur_Key = -1
		self.Empty = pygame.transform.scale(pygame.image.load('Game_Data/Image/Select_Character/Empty.jpg'), (460, 250))

		self.Key_List = [Button(self.Pos_Key[i][0] , self.Pos_Key[i][1] , Empty_Key_Image1 , 1) for i in range(4)]
		self.Key_List.append(Button(self.Pos_Key[4][0] , self.Pos_Key[4][1] , Empty_Key_Image2 , 1))
		self.Key_Text = [cvert(Key_Str[Player_Key[Id - 1][i]]) for i in range(5)]
	
		Left_Image = pygame.transform.scale(pygame.image.load('Game_Data/Image/Select_Character/Left.png'), (20, 20))
		Right_Image = pygame.transform.scale(pygame.image.load('Game_Data/Image/Select_Character/Right.png'), (20, 20))
		self.Left_Button = Button(self.Pos_Left[0] , self.Pos_Left[1] , Left_Image, 1)
		self.Right_Button = Button(self.Pos_Right[0] , self.Pos_Right[1] , Right_Image , 1)
		self.Add_Button = Button(self.Pos_Add[0] , self.Pos_Add[1] , pygame.image.load('Game_Data/Image/Setting_Image/add.png'), 1)
		self.Del_Button = Button(self.Pos_Del[0] , self.Pos_Del[1] , pygame.image.load('Game_Data/Image/Setting_Image/del.png') , 1)
		if Id <= 2:
			self.isAdd = True
		else:
			self.isAdd = False

	def draw(self , Screen):
		Screen.blit(self.Empty , (self.x , self.y))

		if self.isAdd == True:
			if self.Left_Button.isClicked(Screen) == True:
				self.Cur_Skin += (len(self.Skin_List) - 1)
				self.Cur_Skin %= (len(self.Skin_List))

			if self.Right_Button.isClicked(Screen) == True:
				self.Cur_Skin += 1
				self.Cur_Skin %= (len(self.Skin_List)) 

			for i in range(5):
				if self.Key_List[i].isClicked(Screen) == True:
					self.Key_Text[i] = " "
					self.Cur_Key = i
			if self.Cur_Key > -1:
				for i in range(len(Key_Str)):
					if pygame.key.get_pressed()[pygame.key.key_code(Key_Str[i])] == True:
						self.Key_Text[self.Cur_Key] = cvert(Key_Str[i])
						Player_Key[self.Id - 1][self.Cur_Key] = i
						Cur_Key = -1
						break

			if self.Del_Button.isClicked(Screen) == True:
				self.isAdd = False
				self.Cur_Skin = 0
				self.Key_Text = [cvert(Key_Str[Player_Key[self.Id - 1][i]]) for i in range(5)]

		else:
			if self.Add_Button.isClicked(Screen) == True:
				self.isAdd = True

		if self.isAdd == True:
			self.Del_Button.draw(Screen)
			self.Left_Button.draw(Screen)
			self.Right_Button.draw(Screen)
			for i in self.Key_List:
				i.draw(Screen)

			for i in range(5):
				text = font_key.render(self.Key_Text[i] , True , Black)
				text_rect = text.get_rect()
				text_rect.center = (self.Pos_Key[i][0] + (60 + ((i // 4) * 130)) / 2 , self.Pos_Key[i][1] + 13);
				Screen.blit(text , text_rect)

			Screen.blit(self.Skin_List[self.Cur_Skin] , (self.Pos_Skin[0] , self.Pos_Skin[1]))
		else:
			self.Add_Button.draw(Screen)

Character_List = [Character(i) for i in range(1 , 5)]