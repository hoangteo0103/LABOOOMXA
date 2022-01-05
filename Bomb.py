from List_Modunle import *
from Explosions import * 
import pygame
class Bomb():
	def __init__(self , x, y , len) :

		self.delay_start = 20 
		self.counter_start = 0 
		self.counter = 0 
		self.index = 0
		self.delay = 0.06
		self.explosion = []
		self.clock = pygame.time.Clock()
		self.len = len
		self.counter_rear = 0 
		self.delay_rear = 0.06
		self.id = 0 
		for i in range(1 , len + 1) : 
			self.explosion.append(Explosion(x + i * 48 , y , 0))
			self.explosion.append(Explosion(x - i * 48 , y , 1))
			self.explosion.append(Explosion(x , y + i  * 48  , 2))
			self.explosion.append(Explosion(x , y - i * 48 , 3))
		self.frames = bomb_frames
		self.image = self.frames[0]
		self.rect = self.image.get_rect()
		self.rect.x = x 
		self.rect.y = y 
	def draw(self , screen) : 
		self.counter_start+=1
		if(self.counter_start > self.delay_start) :
			self.counter+=1 
			self.counter_rear+=1
			if(self.counter > self.delay) :
				self.counter = 0 
				self.index+=1
				if(self.index >= len(self.frames)) :
					return 
				self.image = self.frames[self.index]
			screen.blit(self.image , self.rect)
			if(self.counter_rear > self.delay_rear) :
				self.counter_rear = 0 
				self.id+=1 
				if(self.id > self.len) :
					return True 
				for i in range(0  , self.id * 4 ) :
					self.explosion[i].draw(screen)
			else : 
				if(self.id >=1) :
					for i in range(0  , self.id * 4 ) :
						self.explosion[i].draw(screen)
			return False
		else :
			screen.blit(self.image , self.rect)
