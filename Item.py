from math import *
from CONST import *

class Item:
	def Rand_
	def __init__(self, X, Y, state):
		self.state = state
		self.frames = Item_Frame[state]
		self.counter = 0
		self.delay = 0.6 
		self.index = 0
		self.image = self.frames[0]
		self.rect = self.image.get_rect()
		self.rect.x = X 
		self.rect.y = Y

	def Draw(self, Screen) :
		self.counter += 1

		if self.counter > self.delay:
			self.counter = 0
			self.index += 1

			if(self.index >= len(self.frames)):
				self.index = 0

		screen.blit(self.image, self.rect)
			
