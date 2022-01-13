from List_Modunle import * 
import pygame 

class Spawn_Effect():
	def __init__(self, x , y):
		self.frames = spawn_frames
		self.index = 0 
		self.counter = 0 
		self.delay = 0.6 
		self.previous_item_list = []
		self.image = self.frames[0]
		self.rect = self.image.get_rect()
		self.rect.x = x 
		self.rect.y = y 
		self.is_render = False 		
	def draw(self , screen) :
		if self.is_render :
			return 
		self.counter+=1 
		if self.counter > self.delay :
			self.counter = 0 
			self.index+=1
			if self.index >= len(self.frames) :
				self.is_render = True
				return 
		self.image = self.frames[self.index]
		screen.blit(self.image , self.rect)
		
		