import pygame 
from CONST import *
import spritesheet
from Bomb import * 
class Player() : 
	def __init__(self , x , y , skin_id) :
		self.reset(x , y , skin_id ) 
		self.bomb = Bomb(-5,-5,0 ,[] ,[] ,[] ,[])
		self.speed = 12
		self.player_lives = 3 
	def update(self , alived , screen , bomb_list, explosion_list , background_list , destrucable_list , undestrucable_list , skin_id , player_lives ) :
		dx = 0 
		dy = 0 
		idle_cooldown = 60
		walk_cooldown = 0.60
		death_cooldown = 5
		if self.bomb.is_denotated() == True :
			self.ok_bomb = True
		if alived == 1 : 
			key = pygame.key.get_pressed()
			if key[Key_List[skin_id][0]] and self.ok_bomb:
				x = (self.rect.x - 264) // 48
				y = (self.rect.y) // 48
				if (self.rect.x - 264) % 48 != 0:
					x += 1
				if (self.rect.y) % 48 != 0:
					y += 1
				self.ok_bomb = False
				self.bomb = Bomb((264 + 48 * x) , y * 48 , 3 , explosion_list, background_list , destrucable_list , undestrucable_list)
				bomb_list.append(self.bomb)
			if key[Key_List[skin_id][1]]:
				dx -= self.speed
				if self.inMovement == 1 :
					self.counter_move += 1
				else :
					self.counter_move = 0 
				self.index_idle = -1
				self.counter_idle = -1 
				self.inMovement = 1 
				self.direction = -1
			elif key[Key_List[skin_id][2]]:
				dx += self.speed
				if self.inMovement == 1 :
					self.counter_move += 1
				else :
					self.counter_move = 0 
				self.index_idle = -1
				self.counter_idle = -1
				self.inMovement = 1
				self.direction = 1
			elif key[Key_List[skin_id][3]]:
				dy -= self.speed
				if self.inMovement == 1 :
					self.counter_move += 1
				else :
					self.counter_move = 0 
				self.index_idle = -1
				self.counter_idle = -1 
				self.inMovement = 1 
				self.direction = -1
			elif key[Key_List[skin_id][4]]:
				dy += self.speed
				if self.inMovement == 1 :
					self.counter_move += 1
				else :
					self.counter_move = 0 
				self.index_idle = -1
				self.counter_idle = -1
				self.inMovement = 1
				self.direction = 1
			if key[Key_List[skin_id][1]] == False and key[Key_List[skin_id][2]] == False and key[Key_List[skin_id][3]] == False and key[Key_List[skin_id][4]] == False:
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
			Num_Collide = 0
			Pos_Collide = self.rect
			for tile in undestrucable_list :
				if(tile[1].colliderect(self.rect)) : 
					Num_Collide += 1
					Pos_Collide = tile[1]
			for tile in destrucable_list :
				if(tile[1].colliderect(self.rect)) : 
					Num_Collide += 1
					Pos_Collide = tile[1]
			if (dx != 0) or (dy != 0):
				if Num_Collide > 0:
					self.rect.x -= dx
					self.rect.y -= dy
					if Num_Collide == 1:
						if abs(Pos_Collide.x - self.rect.x) == Cell_Width:
							if self.rect.y < Pos_Collide.y:
								self.rect.y -= self.speed
							elif self.rect.y > Pos_Collide.y:
								self.rect.y += self.speed
						else:
							if self.rect.x < Pos_Collide.x:
								self.rect.x -= self.speed
							elif self.rect.x > Pos_Collide.x:
								self.rect.x += self.speed

			#handle colision 
			x = (self.rect.x - 264) // 48
			y = (self.rect.y) // 48
			if len(bomb_list) > 0 :
				for t in bomb_list :
					bomb_x = (t.rect.x - 264) // 48
					bomb_y = (t.rect.y) // 48
					if t.rect.colliderect(self.rect) and t.is_denotated() == True  :
						self.alived = 0
						self.player_lives-=1 

			if len(explosion_list) > 0 :
				for t in explosion_list :
					ex_x = (t.rect.x - 264) // 48
					ex_y = (t.rect.y) // 48
					if t.rect.colliderect(self.rect) and t.render == True and t.denotated == False  :
						if self.alived == 1 : 
							self.alived = 0
							self.player_lives-=1  
			screen.blit(self.image, self.rect)
	def reset(self , x , y , skin_id) :
		# idle frame from 0 to 3
		# move frame from 4 to 10
		self.images_idle_right = []
		self.images_idle_left  = []
		self.images_move_right = []
		self.images_move_left =  []
		self.index_move = 0
		self.index_idle = 0  
		self.alived = 1 
		self.ok_bomb = True 
		self.inMovement = 0 
		self.counter_idle = 0
		self.counter_move = 0  
		width = Width_Frames[skin_id]
		height = Heigh_Frames[skin_id]
		sprite_sheet = spritesheet.SpriteSheet(Skin_Image[skin_id])
		for i in range(0,Num_Idle_Frames[skin_id] ) :
			image_idle_right = sprite_sheet.get_image(i,width , height, 10, Black)
			image_idle_right = pygame.transform.scale(image_idle_right , (16 * 3,16 * 3))
			image_idle_left = pygame.transform.flip(image_idle_right, True, False)
			self.images_idle_right.append(image_idle_right)
			self.images_idle_left.append(image_idle_left)
		for i in range(Num_Idle_Frames[skin_id],Num_Move_Frames[skin_id] ) :
			image_move_right = sprite_sheet.get_image(i, width, height,10, Black)
			image_move_right = pygame.transform.scale(image_move_right , (16 * 3,16 * 3))
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