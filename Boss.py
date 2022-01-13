from List_Modunle import * 
import pygame 
class Boss():
	def __init__(self, x , y ):
		self.frames = boss_frames
		self.index = 0 
		self.counter = 0 
		self.delay = 0.6 
		self.item_counter = 0 
		self.item_delay = 100 
		self.image = self.frames[0]
		self.rect = self.image.get_rect()
		self.rect.x = x 
		self.rect.y = y 
	def draw(self , screen) :
		ok = False 
		self.counter+=1 
		self.item_counter+=1 
		if self.item_counter > self.item_delay : 
			self.item_counter = 0 
			ok = True 
		if self.counter > self.delay :
			self.counter = 0 
			self.index+=1
			if self.index >= len(self.frames) :
				self.index = 0 
		self.image = self.frames[self.index]
		screen.blit(self.image , self.rect)
		return ok