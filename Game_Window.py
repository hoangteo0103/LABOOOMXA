from List_Modunle import *
import Main_Menu_Window

def Run() :
	Game_Screen = pygame.display.set_mode((Game_Window_Width, Game_Window_Height))
	Player1 = Player(312 , 48)
	
	bomb_list = []
	explosion_list = []
	destrucable_list = []
	undestrucalbe_list = []
	background_list = []
	# Set the caption of the screen
	pygame.display.set_caption('LABOOMXA')
	  
	# Update the display using flip
	pygame.display.flip()
	  
	# Variable to keep our game loop running
	running = True	
	clock = pygame.time.Clock()

	Board  = Play_Board(1 ,background_list , destrucable_list , undestrucalbe_list )

	# game loop
	death_counter = [0 , 0 , 0 , 0 ]
	death_cooldown = 60 
	while running:
		clock.tick(10)
		for event in pygame.event.get():
			# Check for QUIT event      
			if event.type == pygame.QUIT:
				running = False
				Main_Menu_Window.Run()
				exit()


		Game_Screen.fill(Black)
		Board.Draw_Board(Game_Screen ,background_list , destrucable_list , undestrucalbe_list)
		if len(explosion_list) > 0 :
				for t in explosion_list :
					if t.is_denotated() == True :
						explosion_list.remove(t)
		if len(bomb_list) > 0 :
			for t in bomb_list :
				if t.draw(Game_Screen,background_list , destrucable_list , undestrucalbe_list) == True :
					bomb_list.remove(t)
		if(Player1.alived == 0) :
			death_counter[0]+=1
			if(death_counter[0] > death_cooldown) :
				death_counter[0] = 0 
				Player1.alived = 1 
				Player1.reset(312 , 48)
		if(Player1.alived == 1 ) :
			Player1.update(Player1.alived,Game_Screen , bomb_list , explosion_list , background_list , destrucable_list , undestrucalbe_list )
		
		
		pygame.display.update()
