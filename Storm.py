from List_Modunle import * 
import pygame 
 
class Storm() :
 	def __init__(self , x , y , dir ) :
 		self.dir = dir
 		self.frames = storm_frames
 		self.index = 0 
 		self.counter = 0 
 		self.delay = 0.6 
 		self.speed = 24 
 		self.image = self.frames[0]
 		self.stop = False 
 		self.rect = self.image.get_rect()
 		self.rect.x = x
 		self.rect.y = y 
 		if self.dir == -1 :
 			self.rect.x-=48
 		elif self.dir == 1 :
 			self.rect.x+=48
 		elif self.dir == 2 :
 			self.rect.y-=48
 		else :
 			self.rect.y+=48
 	def draw(self , screen , destrucable_list , undestrucable_list ) : 
 		if self.stop == True :
 			return True
 		
 		for tile in destrucable_list :
 			if(tile[1].colliderect(self.rect)) :
 				self.stop = True 
 				return True 
 		for tile in undestrucable_list :
 			if(tile[1].colliderect(self.rect)) :
 				self.stop = True 
 				return
 		self.counter+=1 
 		if self.counter > self.delay :
 			self.counter = 0 
 			self.index+=1
 			if self.dir == -1 :
 				self.rect.x-=self.speed
 			elif self.dir == 1 :
 				self.rect.x+=self.speed
 			elif self.dir == 2 :
 				self.rect.y-=self.speed
 			elif self.dir == -2:
 				self.rect.y+=self.speed
 			for tile in destrucable_list :
 				if(tile[1].colliderect(self.rect)) :
 					self.stop = True 
 					return
 			for tile in undestrucable_list :
 				if(tile[1].colliderect(self.rect)) :
 					self.stop = True 
 					return
 			if self.index >= len(self.frames) :
 				self.index = 0 
 			self.images = self.frames[self.index]
 		screen.blit(self.image , self.rect)
 		return False 