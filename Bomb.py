from List_Modunle import *
from Explosions import * 
import pygame
class Bomb():
	def __init__(self , x, y , len , explosion_list) :

		self.denotated = False 
		self.delay_start = 20 
		self.counter_start = 0 
		self.counter = 0 
		self.index = 0
		self.delay = 1
		self.explosion = []
		self.clock = pygame.time.Clock()
		self.len = len
		self.counter_rear = 0 
		self.delay_rear = 2
		self.id = 0 
		for i in range(1 , len + 1) : 
			left  = Explosion(x + i * 48 , y , 0)
			right = Explosion(x - i * 48 , y , 1)
			up    = Explosion(x , y - i * 48 , 3)
			down  =  Explosion(x , y + i  * 48  , 2)
			explosion_list.append(left)
			explosion_list.append(right)
			explosion_list.append(up)
			explosion_list.append(down)
			self.explosion.append(left)
			self.explosion.append(right)
			self.explosion.append(up)
			self.explosion.append(down)
		self.frames = bomb_frames
		self.image = self.frames[0]
		self.rect = self.image.get_rect()
		self.rect.x = x 
		self.rect.y = y 
	def draw(self , screen) : 
		self.counter_start+=1
		if(self.counter_start > self.delay_start) :
			self.counter+=1 
			self.denotated = True 
			self.counter_rear+=1
			if(self.counter_rear > self.delay_rear) :
				self.counter_rear = 0 
				self.id+=1 
				if(self.id > self.len) :
					for i in range(0  , (self.id - 1 ) * 4 ) :
						self.explosion[i].denotated = True 
					return True 
				for i in range(0  , self.id * 4 ) :
					self.explosion[i].draw(screen)
			if(self.counter > self.delay) :
				self.counter = 0 
				self.index+=1
				if(self.index >= len(self.frames)) :
					print("gg")
					return True
				self.image = self.frames[self.index]
			screen.blit(self.image , self.rect)
			
		else :
			screen.blit(self.image , self.rect)
		return False
	def is_denotated(self) :
		return self.denotated