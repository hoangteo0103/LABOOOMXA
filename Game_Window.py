from List_Modunle import *
import Main_Menu_Window

def Run() :
	Player1 = Player(100 , 100)
	Game_Screen = pygame.display.set_mode((Game_Window_Width, Game_Window_Height))

	# Set the caption of the screen
	pygame.display.set_caption('LABOOMXA')
	  
	# Update the display using flip
	pygame.display.flip()
	  
	# Variable to keep our game loop running
	running = True	
	clock = pygame.time.Clock()

	# game loop
	while running:
		clock.tick(10)
		for event in pygame.event.get():
			# Check for QUIT event      
			if event.type == pygame.QUIT:
				running = False
				Main_Menu_Window.Run()
				exit()


		Game_Screen.fill(Black)
		Player1.update(1,Game_Screen)
		pygame.display.update()
