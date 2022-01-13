from List_Modunle import *
import pygame 
from button import * 
Image = []
Board = [[0 for i in range(17)] for j in range(15)]
clicked = [[False for i in range(17)] for j in range(15)]
screen = pygame.display.set_mode((20 * 48 , 20 * 48))
for i in range(8):
	Image_tmp = pygame.image.load(f'Game_Data/Image/Map_2/tile_{i}.png')
	Image_tmp = pygame.transform.scale(Image_tmp, (Cell_Width, Cell_Height))
	Image.append(Image_tmp)
running = True 
gg = Button( 18*48, 0 * 48 ,Image[0] , 1)
Board_File = open(f'Game_Data/Image/Map_2/Map.txt')
Str = Board_File.read()

for t in range(0, len(Str)):
	x = t // 18
	y = t % 18
	if y == 17: continue
	Board[x][y] = int(Str[t])
while running:
	for event in pygame.event.get():
		# Check for QUIT event      
		if event.type == pygame.QUIT:
			running = False
			break
	

	screen.fill(Black)
	for i in range(15) :
		for j in range(17) :
			img = Image[Board[i][j]]
			rect = img.get_rect()
			rect.x = j * 48 
			rect.y = i * 48
			action = False
			pos = pygame.mouse.get_pos()
			if rect.collidepoint(pos) :
				if(pygame.mouse.get_pressed()[0] == 1  and clicked[i][j] == False) :
					clicked[i][j] = True
					action = True 
			if(pygame.mouse.get_pressed()[0] == 0) : 
				clicked[i][j] = False 
			if action :
				Board[i][j] = (Board[i][j] + 7) % 8
			img = Image[Board[i][j]]
			rect = img.get_rect()
			rect.x = j * 48 
			rect.y = i * 48
			screen.blit(Image[0] , rect)
			screen.blit(img , rect) 

	gg.draw(screen)
	if (gg.isClicked(screen)) :
		with open('Game_Data/Image/Map_2/Map.txt', "w") as o:
			for i in range(15) :
				for j in range(17) :
					o.write(str(Board[i][j]))
				o.write('\n')		
			break 
	pygame.display.update()




