from List_Modunle import *
import Main_Menu_Window

def Run() :
	Game_Screen = pygame.display.set_mode((Game_Window_Width, Game_Window_Height))
	Player1 = Player(100 , 100)
	Bomb1 = Bomb(100 , 200 , 3)

	# Set the caption of the screen
	pygame.display.set_caption('LABOOMXA')
	  
	# Update the display using flip
	pygame.display.flip()
	  
	# Variable to keep our game loop running
	running = True	
	clock = pygame.time.Clock()

	Board  = Play_Board(1)

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
		Board.Draw_Board(Game_Screen)
		Player1.update(1,Game_Screen)
		Bomb1.draw(Game_Screen)
		pygame.display.update()