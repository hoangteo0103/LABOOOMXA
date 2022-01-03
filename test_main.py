
import pygame

pygame.init()

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Spritesheets')

sprite_sheet_image = pygame.image.load('doux.png')
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)

BG = (50, 50, 50)
BLACK = (0, 0, 0)

frame = [sprite_sheet.get_image(i, 24, 24, 5, BLACK) for i in range(0 , 24) ]

clock = pygame.time.Clock()

run = True
while run:

	#update background
	screen.fill(BG)

	#show frame image


	#event handler
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	for i in range(0,24) :
		screen.fill(BG)
		screen.blit(frame[i], (i * 24 , 0))
		pygame.display.update()
		clock.tick(10)

pygame.quit()

