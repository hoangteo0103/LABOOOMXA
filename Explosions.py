from List_Modunle import *
import pygame
import random 
from Item import *
class Explosion():
	def __init__(self , x, y , dir , is_render ) :
		self.denotated = False 
		self.counter = 0 
		self.index = 0
		self.delay = 6
		self.render = False 
		self.is_render = is_render
		self.frames = explosion_frames[dir]
		self.image = self.frames[0]
		self.rect = self.image.get_rect()
		self.rect.x = x 
		self.rect.y = y 
		self.stop = False 
		self.cc = 1 
	def draw(self , screen , background_list , destrucable_list , undestrucable_list , item_list ) : 
		if(self.is_render == True or self.stop == True) :
			return 
		self.render = True 
		self.counter+=1 
		for tile in undestrucable_list :
			if(tile[1].colliderect(self.rect)) : 
				return 

		# Random Item
		
		for tile in destrucable_list :
			if(tile[1].colliderect(self.rect)) :
				destrucable_list.remove(tile)
				background_list.append((background_list[0][0] ,tile[1]))
				is_item = random.randint(0,1)
				if is_item == 1 :
					type_item = random.randint(1, 100)
					if type_item >= 1 and type_item <= 10 :
						type_item = 0
					elif type_item >= 11 and type_item <= 20 :
						type_item = 2 
					elif type_item >= 21 and type_item <= 40 :
						type_item = 1 
					elif type_item >= 41 and type_item <= 60 :
						type_item = 3
					elif type_item >= 61 and type_item <= 80 :
						type_item = 4 
					elif type_item >=  81 and type_item <= 100 : 
						type_item = 5 
					item = Item(tile[1].x , tile[1].y , type_item)
					item_list.append(item)
				self.stop = True 
				return 
		for tile in item_list : 
			if tile.rect.colliderect(self.rect) :
				item_list.remove(tile) 
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