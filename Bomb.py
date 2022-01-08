from List_Modunle import *
from Explosions import * 
import pygame
class Bomb():
	def __init__(self , x, y , len , explosion_list , background_list , destrucable_list , undestrucable_list , item_list ) :

		self.frames = bomb_frames
		self.image = bomb_image 
		self.rect = self.image.get_rect()
		self.rect.x = x 
		self.rect.y = y 
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
		self.delay_rear = 1
		self.id = 0 
		previous = [False for i in range(1,5)]
		for i in range(1 , len + 1) : 
			for id in range (0 , 4 ) : 
				new_x = x 
				new_y = y
				if id == 0 :
					new_x = x + i * 48 
				if id == 1 :
					new_x = x - i * 48
				if id == 2 :
					new_y = y - i * 48
				if id == 3 :
					new_y = y + i * 48
				img  =  Explosion(new_x , new_y  , id , previous[id] )
				rect = img.image.get_rect()
				rect.x = new_x 
				rect.y = new_y
				self.explosion.append(img)
				explosion_list.append(img)
				for tile in undestrucable_list :
					if(tile[1].colliderect(rect)) : 
						 previous[id] = True
				for tile in destrucable_list :
					if(tile[1].colliderect(rect)) :
						previous[id] = True
				
		
		
	def draw(self , screen , background_list , destrucable_list , undestrucable_list , item_list) : 
		for tile in undestrucable_list :
			if(tile[1].colliderect(self.rect)) : 
				return 
		for tile in destrucable_list :
			if(tile[1].colliderect(self.rect)) : 
				return 
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
					self.explosion[i].draw(screen,background_list , destrucable_list , undestrucable_list , item_list)
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