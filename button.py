import pygame
from List_Modunle import *

class Button() :
	def __init__(self , x , y , image , scale):
		width = image.get_width()
		height = image.get_height() 
		self.image = pygame.transform.scale(image , (int(width * scale) , int(height * scale)))
		self.image.set_colorkey(Black)

		self.rect = self.image.get_rect()
		self.rect.topleft = (x,y)
		self.clicked = False

	def draw(self , screen):
		pos = pygame.mouse.get_pos()

		if self.rect.collidepoint(pos):
			self.image.set_alpha(255)
			print(1)
		else:
			self.image.set_alpha(220)
		screen.blit(self.image , (self.rect.x , self.rect.y))

	def isClicked(self , screen): 
		action = False 
		pos = pygame.mouse.get_pos()
		if self.rect.collidepoint(pos) :
			if(pygame.mouse.get_pressed()[0] == 1  and self.clicked == False) :
				self.clicked = True
				action = True 
		if(pygame.mouse.get_pressed()[0] == 0) : 
			self.clicked = False 
		return action 