import pygame 
from CONST import *
import spritesheet
from Bomb import * 
from Storm import *
class Player() : 
	def __init__(self , x , y , skin_id) :
		self.reset(x , y , skin_id ) 
		self.player_bomb_list = [] 
		self.speed = 12
		self.player_lives = 3 
		self.shield = 0 
		self.power = 1
		self.number_bombs = 1 
		self.storm = 0
		self.portal_cooldown = 20 
		self.portal_counter  = 0 
		self.is_through_portal = False 
		self.storm_cooldown = 0
		self.shield_cooldown = 0
	def update(self , alived , screen , bomb_list, explosion_list , background_list , destrucable_list , undestrucable_list , storm_list ,portal_list , item_list , skin_id , player_lives ) :
		dx = 0 
		dy = 0 
		idle_cooldown = 60
		walk_cooldown = 0.60
		death_cooldown = 5
		for t in self.player_bomb_list :
			if t.is_denotated() == True : 
				self.player_bomb_list.remove(t)
		storm = False

		if(self.storm_cooldown > 0): self.storm_cooldown -= 1
		if(self.shield_cooldown > 0): self.shield_cooldown -= 1

		if(self.shield_cooldown == 0): self.shield = 0

		if alived == 1 : 
			key = pygame.key.get_pressed()
			if key[Key_List[Player_Key[skin_id][4]]] :
				if self.storm == 1 :
					dire = 3 
					if key[Key_List[Player_Key[skin_id][1]]]:
						dire = -1 
					if key[Key_List[Player_Key[skin_id][3]]]:
						dire = 1 
					if key[Key_List[Player_Key[skin_id][0]]]:
						dire = -2 
					if key[Key_List[Player_Key[skin_id][2]]]:
						dire = 2 
					if dire!=3  :
						storm = True
						storm_list.append(Storm(self.rect.x  , self.rect.y ,dire))
						self.storm = 0
						self.storm_cooldown = 10
				elif (len(self.player_bomb_list) < self.number_bombs and self.storm_cooldown == 0):
					x = (self.rect.x - 264) // 48
					y = (self.rect.y) // 48
					if (self.rect.x - 264) % 48 != 0:
						x += 1
					if (self.rect.y) % 48 != 0:
						y += 1
					bomb_now = Bomb((264 + 48 * x) , y * 48 , self.power , explosion_list, background_list , destrucable_list , undestrucable_list , item_list )
						
					kq = True
					for i in self.player_bomb_list:
						X = (i.rect.x - 264) // 48
						Y = (i.rect.y) // 48
						if(x == X and y == Y): kq = False

					if kq == True:
						bomb_list.append([bomb_now , 0])
						self.player_bomb_list.append(bomb_now)
			if key[Key_List[Player_Key[skin_id][1]]] and not storm:
				dx -= self.speed
				if self.inMovement == 1 :
					self.counter_move += 1
				else :
					self.counter_move = 0 
				self.index_idle = -1
				self.counter_idle = -1 
				self.inMovement = 1 
				self.direction = -1
			elif key[Key_List[Player_Key[skin_id][3]]] and not storm:
				dx += self.speed
				if self.inMovement == 1 :
					self.counter_move += 1
				else :
					self.counter_move = 0 
				self.index_idle = -1
				self.counter_idle = -1
				self.inMovement = 1
				self.direction = 1
			elif key[Key_List[Player_Key[skin_id][0]]] and not storm:
				dy -= self.speed
				if self.inMovement == 1 :
					self.counter_move += 1
				else :
					self.counter_move = 0 
				self.index_idle = -1
				self.counter_idle = -1 
				self.inMovement = 1 
				self.direction = -2
			elif key[Key_List[Player_Key[skin_id][2]]]and not storm:
				dy += self.speed
				if self.inMovement == 1 :
					self.counter_move += 1
				else :
					self.counter_move = 0 
				self.index_idle = -1
				self.counter_idle = -1
				self.inMovement = 1
				self.direction = 2
			if key[Key_List[Player_Key[skin_id][1]]] == False and key[Key_List[Player_Key[skin_id][2]]] == False and key[Key_List[Player_Key[skin_id][3]]] == False and key[Key_List[Player_Key[skin_id][0]]] == False:
				self.inMovement = 0
				self.counter_move = 0 
				self.index_idle = (self.index_idle + 1) % 4
				self.counter_idle+=1
				if self.direction == 1 or self.direction == 2 :
					self.image = self.images_idle_right[self.index_idle]
				if self.direction == -1 or self.direction == -2 :
					self.image = self.images_idle_left[self.index_idle]


			#handle animation
			if self.inMovement == 1 :
				if self.counter_move > walk_cooldown:
					self.counter_move = 0	
					self.index_move += 1
					if self.index_move >= len(self.images_move_right):
						self.index_move= 0
					if self.direction == 1 or self.direction == 2:
						self.image = self.images_move_right[self.index_move]
					if self.direction == -1 or self.direction == -2 :
						self.image = self.images_move_left[self.index_move]
			else :
				if self.counter_idle > idle_cooldown:
					self.counter_idle = 0	
					self.index_idle += 1
					if self.index_idle >= len(self.images_idle_right):
						self.index_idle = 0
					if self.direction == 1 or self.direction == 2 :
						self.image = self.images_idle_right[self.index_idle]
					if self.direction == -1 or self.direction == -2 :
						self.image = self.images_idle_left[self.index_idle]
		#update portal counter 
			if self.is_through_portal == True :
				self.portal_counter+=1
				if(self.portal_counter > self.portal_cooldown ) :
					self.portal_counter = 0
					self.is_through_portal = False 
			 


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
			for tile in bomb_list:
				if tile[1] == 1:
					if(tile[0].rect.colliderect(self.rect)) : 
						Num_Collide += 1
						Pos_Collide = tile[0].rect
			if (dx != 0) or (dy != 0):
				if Num_Collide > 0:
					self.rect.x -= dx
					self.rect.y -= dy
					if Num_Collide == 1:
						if abs(Pos_Collide.x - self.rect.x) == Cell_Width:
							if self.rect.y < Pos_Collide.y:
								if self.rect.y % 12 == 0:
									self.rect.y -= 12
								else:
									self.rect.y -= self.rect.y % 12
							elif self.rect.y > Pos_Collide.y:
								self.rect.y += 12
								if self.rect.y % 12 != 0:
									self.rect.y -= self.rect.y % 12
						elif abs(Pos_Collide.y - self.rect.y) == Cell_Height:
							if self.rect.x < Pos_Collide.x:
								if self.rect.x % 12 == 0:
									self.rect.x -= 12
								else:
									self.rect.x -= self.rect.x % 12
							elif self.rect.x > Pos_Collide.x:
								self.rect.x += 12
								if self.rect.x % 12 != 0:
									self.rect.x -= self.rect.x % 12
						else:
							while Pos_Collide.colliderect(self.rect) == False:
								self.rect.x += (dx // self.speed)
								self.rect.y += (dy // self.speed)
							self.rect.x -= (dx // self.speed)
							self.rect.y -= (dy // self.speed)

			#handle colision 
			is_collission  = 0 
			if len(bomb_list) > 0 :
				for t in bomb_list :
					if t[0].rect.colliderect(self.rect) and t[0].is_denotated() == True  :
						is_collission = 1 
						if (self.shield == 1) :
							bomb_list.remove(t)
			if len(explosion_list) > 0 :
				for t in explosion_list :
					if t.rect.colliderect(self.rect) and t.render == True and t.denotated == False  :
						is_collission = 1 
						if (self.shield == 1) :
							explosion_list.remove(t)
			if len(storm_list) > 0 :
				for t in storm_list :
					if t.rect.colliderect(self.rect) :
						is_collission = 1 
						if (self.shield == 1) :
							storm_list.remove(t)
			if is_collission == 1 :
				if(self.shield == 1) :
					self.shield = 0
				else :
					self.shield = 0
					self.alived = 0 
					self.player_lives -= 1					
			if len(item_list) > 0 :
				for t in item_list :
					if t.rect.colliderect(self.rect) :
						if(t.state == 0) :
							self.player_lives+=1
							item_list.remove(t)
						if(t.state == 1) :
							self.power += 1
							item_list.remove(t)
						if(t.state == 2) :
							self.shield = 1 
							self.shield_cooldown = 300
							item_list.remove(t)
						if(t.state == 3) :
							self.storm = 1 
							item_list.remove(t)
						if t.state == 4 :
							self.speed += 2
							self.speed = min(self.speed , 24)
							item_list.remove(t)
						if t.state == 5 :
							self.number_bombs += 1
							item_list.remove(t)
			if(len(portal_list) > 0) and self.is_through_portal == False :
				for i in range(2) :
					if(self.rect.colliderect(portal_list[i].rect)) :
						self.rect.x = portal_list[i ^ 1 ].rect.x
						self.rect.y = portal_list[i ^ 1 ].rect.y
						self.is_through_portal = True 
						break 

			if(self.shield == 1) :
				screen.blit(bubble_image, self.rect)
			screen.blit(self.image, self.rect)
	def reset(self , x , y , skin_id) :
		# idle frame from 0 to 3
		# move frame from 4 to 10
		self.images_idle_right = []
		self.images_idle_left  = []
		self.images_move_right = []
		self.images_move_left =  []
		self.bomb_list = [] 
		self.index_move = 0
		self.index_idle = 0  
		self.alived = 1 
		self.ok_bomb = True 
		self.number_bombs = 1 
		self.inMovement = 0 
		self.counter_idle = 0
		self.counter_move = 0
		self.power = 1  
		self.portal_cooldown = 20 
		self.portal_counter  = 0 
		self.is_through_portal = False 
		self.storm = 0 
		self.speed = 12
		self.skin_id = skin_id 
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