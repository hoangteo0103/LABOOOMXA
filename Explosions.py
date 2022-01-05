from List_Modunle import *
import pygame
class Explosion():
	def __init__(self , x, y , dir) :
		self.denotated = False 
		self.counter = 0 
		self.index = 0
		self.delay = 6
		self.render = False 
		self.frames = explosion_frames[dir]
		self.image = self.frames[0]
		self.rect = self.image.get_rect()
		self.rect.x = x 
		self.rect.y = y 
		self.cc = 1 
	def draw(self , screen) : 
		self.render = True 
		self.counter+=1 
		if(self.counter > self.delay) :
			self.counter = 0 
			self.index+=1
			if(self.index >= len(self.frames))  :
				self.denotated = True 
				self.cc = 2 
				return 
			self.image = self.frames[self.index]
		screen.blit(self.image , self.rect)
	def is_denotated(self) :
		return self.denotated