from List_Modunle import *
import pygame
class Explosion():
	def __init__(self , x, y , dir ) :

		self.counter = 0 
		self.index = 0
		self.delay = 6
		self.frames = explosion_frames[dir]
		self.image = self.frames[0]
		self.rect = self.image.get_rect()
		self.rect.x = x 
		self.rect.y = y 
	def draw(self , screen) : 
		self.counter+=1 
		if(self.counter > self.delay) :
			self.counter = 0 
			self.index+=1
			if(self.index >= len(self.frames)) :
				return 
			self.image = self.frames[self.index]
		screen.blit(self.image , self.rect)

