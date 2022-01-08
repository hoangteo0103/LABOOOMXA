from List_Modunle import *

class Item:
	def __init__(self, X, Y, state):
		self.state = state
		self.counter = 0
		self.delay = 0.6 
		self.index = 0
		self.sprite_sheet  = SpriteSheet(Item_Frame[state])
		self.image = self.sprite_sheet.get_image(0 , 1024 , 1024 , 1 , Black)
		self.image = pygame.transform.scale(self.image , (48 ,48))
		self.rect = self.image.get_rect()
		self.rect.x = X 
		self.rect.y = Y

	def draw(self, screen) :
		self.counter += 1

		if self.counter > self.delay:
			self.counter = 0
			self.index += 1

			if(self.index >= 3):
				self.index = 0

		self.image = self.sprite_sheet.get_image(self.index , 1024 , 1024 , 1 , Black)
		self.image = pygame.transform.scale(self.image , (48 ,48))
		screen.blit(self.image, self.rect)
			
