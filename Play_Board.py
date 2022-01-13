from List_Modunle import *
import random 
class Play_Board():
	Image = []
	Board = [[-1 for i in range(20)] for j in range(20)]

	def __init__(self, Map_State, background_list , destrucable_list , undestrucable_list):
		for i in range(8):
			Image_tmp = pygame.image.load(f'Game_Data/Image/Map_{Map_State}/tile_{i}.png')
			Image_tmp = pygame.transform.scale(Image_tmp, (Cell_Width, Cell_Height))
			self.Image.append(Image_tmp)

		self.counter_portal = 200
		self.portal_cooldown = 200
		Board_File = open(f'Game_Data/Image/Map_{Map_State}/Map.txt')
		Str = Board_File.read()

		for t in range(0, len(Str)):
			x = t // 18
			y = t % 18
			if y == 17: continue
			self.Board[x][y] = int(Str[t])
			if self.Board[x][y] == 7 :
				img = self.Image[7] 
				rect = img.get_rect()
				rect.x = 264 + y * Cell_Width
				rect.y = x * Cell_Height
				undestrucable_list.append( (img , rect) )
			elif self.Board[x][y] <=6 and self.Board[x][y] >=1 :
				img = self.Image[self.Board[x][y]]
				rect = img.get_rect()
				rect.x = 264 + y * Cell_Width
				rect.y = x * Cell_Height
				destrucable_list.append((img , rect))
			elif self.Board[x][y] == 0 :
				img = self.Image[0]
				rect = img.get_rect()
				rect.x = 264 + y * Cell_Width
				rect.y = x * Cell_Height
				background_list.append((img , rect))
	def Print_Board(self):
		for i in range(0, 15):
			for j in range(0, 17):
				print(self.Board[i][j], end = ' ')
			print()

	def Draw_Board(self, screen , background_list , destrucable_list , undestrucable_list , portal_list ):
		self.counter_portal+=1 
		if self.counter_portal > self.portal_cooldown : 
			self.counter_portal = 0 
			len_list = len(background_list)
			x = random.randint(0,len_list - 1) 
			y = random.randint(0,len_list - 1)
			while x == y :
				y = random.randint(0,len_list - 1)
			for tile in background_list :
				screen.blit(tile[0] , tile[1])
			portal_list.clear()
			portal_list.append(Portal(background_list[x][1].x , background_list[x][1].y))
			portal_list.append(Portal(background_list[y][1].x , background_list[y][1].y))
		else :
			for tile in background_list :
				screen.blit(tile[0] , tile[1])
		for t in portal_list :
			t.draw(screen)
		for tile in destrucable_list :
			screen.blit(self.Image[0] , tile[1])
			screen.blit(tile[0] , tile[1])
		for tile in undestrucable_list :
			screen.blit(self.Image[0] , tile[1])
			if not (tile[1].x >= 600 and tile[1].y >= 288 and tile[1].x <= 744 and tile[1].y <= 432) :
				screen.blit(tile[0] , tile[1])
		


