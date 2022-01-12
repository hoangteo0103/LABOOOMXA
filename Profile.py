from List_Modunle import * 
import pygame 
class Profile() :
	def __init__(self , Player_List) :
		self.number_of_player = len(Player_List)
		self.List = Player_List
	def draw(self ,screen) :
		pos = 0
		for i in range(0 , self.number_of_player) : 
			screen.blit(Profile_Image ,(0,pos))
			text = font_player.render("Player " + str(i + 1 ) , True, White)
			screen.blit(text , (30, pos + 15) )
			screen.blit(Heart_Image , (167 , 15 + pos))
			screen.blit(Speed_Image , (172 , 55 + pos))
			screen.blit(Bomb_Image , (174 , 95 + pos))
			screen.blit(Potion_Image , (174 , 135 + pos))
			screen.blit(Skin_Profile_Image[self.List[i].skin_id] , (10 , pos + 20))
			#Lives 
			text = font_item.render(": " + str(self.List[i].player_lives) , True , Green)
			screen.blit(text , (205 , 22 + pos))
			#Speed 
			text = font_item.render(": " + str(self.List[i].speed) , True , Green)
			screen.blit(text , (205 , 55 + pos))
			#Bomb 
			text = font_item.render(": " + str(self.List[i].number_bombs) , True , Green)
			screen.blit(text , (205 , 95 + pos))
			#Potion 
			text = font_item.render(": " + str(self.List[i].power) , True , Green)
			screen.blit(text , (205 , 135 + pos))

			pos+=180
