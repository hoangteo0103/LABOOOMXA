import pygame 
from CONST import *
import spritesheet

class Player() : 
	def __init__(self , x , y) :
		self.reset(x , y) 
	def update(self , alived , screen) :
		dx = 0 
		dy = 0 
		idle_cooldown = 60
		walk_cooldown = 0.60
		death_cooldown = 5
		if alived == 1 : 
			key = pygame.key.get_pressed()
			if key[pygame.K_LEFT]:
				dx -= 25
				if self.inMovement == 1 :
					self.counter_move += 1
				else :
					self.counter_move = 0 
				self.index_idle = -1
				self.counter_idle = -1 
				self.inMovement = 1 
				self.direction = -1
			if key[pygame.K_RIGHT]:
				dx += 25
				if self.inMovement == 1 :
					self.counter_move += 1
				else :
					self.counter_move = 0 
				self.index_idle = -1
				self.counter_idle = -1
				self.inMovement = 1
				self.direction = 1
			if key[pygame.K_UP]:
				dy -= 25
				if self.inMovement == 1 :
					self.counter_move += 1
				else :
					self.counter_move = 0 
				self.index_idle = -1
				self.counter_idle = -1 
				self.inMovement = 1 
				self.direction = -1
			if key[pygame.K_DOWN]:
				dy += 25
				if self.inMovement == 1 :
					self.counter_move += 1
				else :
					self.counter_move = 0 
				self.index_idle = -1
				self.counter_idle = -1
				self.inMovement = 1
				self.direction = 1
			if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False and key[pygame.K_UP] == False and key[pygame.K_DOWN] == False:
				self.inMovement = 0
				self.counter_move = 0 
				self.index_idle = (self.index_idle + 1) % 4
				
				self.counter_idle+=1
				if self.direction == 1:
					self.image = self.images_idle_right[self.index_idle]
				if self.direction == -1:
					self.image = self.images_idle_left[self.index_idle]


			#handle animation
			if self.inMovement == 1 :
				if self.counter_move > walk_cooldown:
					self.counter_move = 0	
					self.index_move += 1
					if self.index_move >= len(self.images_move_right):
						self.index_move= 0
					if self.direction == 1:
						self.image = self.images_move_right[self.index_move]
					if self.direction == -1:
						self.image = self.images_move_left[self.index_move]
			else :
				if self.counter_idle > idle_cooldown:
					self.counter_idle = 0	
					self.index_idle += 1
					if self.index_idle >= len(self.images_idle_right):
						self.index_idle = 0
					if self.direction == 1:
						self.image = self.images_idle_right[self.index_idle]
					if self.direction == -1:
						self.image = self.images_idle_left[self.index_idle]
		#update player coordinates
			self.rect.x += dx
			self.rect.y += dy
			screen.blit(self.image, self.rect)
	def reset(self , x , y) :
		# idle frame from 0 to 3
		# move frame from 4 to 10
		self.images_idle_right = []
		self.images_idle_left  = []
		self.images_move_right = []
		self.images_move_left =  []
		self.index_move = 0
		self.index_idle = 0  
		self.alived = 1 
		self.inMovement = 0 
		self.counter_idle = 0
		self.counter_move = 0  
		sprite_sheet = spritesheet.SpriteSheet(Skin_Image[0])
		for i in range(0,4 ) :
			image_idle_right = sprite_sheet.get_image(i, 24, 24, 5, Black)
			image_idle_left = pygame.transform.flip(image_idle_right, True, False)
			self.images_idle_right.append(image_idle_right)
			self.images_idle_left.append(image_idle_left)
		for i in range(4,11 ) :
			image_move_right = sprite_sheet.get_image(i, 24, 24, 5, Black)
			image_move_left = pygame.transform.flip(image_move_right, True, False)
			self.images_move_right.append(image_move_right)
			self.images_move_left.append(image_move_left)
		self.image = self.images_idle_right[self.index_idle]
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.direction = 0