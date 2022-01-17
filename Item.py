from List_Modunle import *

class Item:
	def __init__(self, X, Y, state):
		self.state = state
		self.counter = 0
		self.delay = 0.6 
		self.index = 0
		self.counter_erase = 0 
		self.time_erase = 100 
		self.sprite_sheet  = SpriteSheet(Item_Frame[state])
		self.width = Item_Frame_Size[state][0]
		self.height = Item_Frame_Size[state][1]
		self.image = self.sprite_sheet.get_image(0 , self.width , self.height , 1 , Black)
		self.image = pygame.transform.scale(self.image , (48 ,48))
		self.rect = self.image.get_rect()
		self.rect.x = X 
		self.rect.y = Y

	def draw(self, screen) :
		self.counter_erase+=1
		if self.counter_erase > self.time_erase : 
			return True 
		self.counter += 1

		if self.counter > self.delay:
			self.counter = 0
			self.index += 1

			if(self.index >= Number_Item_Frame[self.state]):
				self.index = 0

		self.image = self.sprite_sheet.get_image(self.index , self.width , self.height , 1 , Black)
		self.image = pygame.transform.scale(self.image , (48 ,48))
		screen.blit(self.image, self.rect)
		return False 
