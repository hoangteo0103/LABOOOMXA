from List_Modunle import *
import Main_Menu_Window

def Run() :
	Game_Screen = pygame.display.set_mode((Game_Window_Width, Game_Window_Height))
	Player_List = [Player(984 , 48 , 0) , Player(312 , 48 , 1) , Player(312 , 624 , 2) , Player(984 , 624 , 3)]
	Player_Coord = [(984 , 48) , (312 , 48) , (312 , 624) , (984 , 624)]

	bomb_list = []
	explosion_list = []
	destrucable_list = []
	undestrucalbe_list = []
	background_list = []
	item_list = []
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
	player_lives  = [3,  3 , 3 , 3 ]
	death_cooldown = 25
	item_list = []
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
				if t.draw(Game_Screen,background_list , destrucable_list , undestrucalbe_list , item_list) == True :
					bomb_list.remove(t)
		if len(item_list) > 0 :
			for t in item_list :
				t.draw(Game_Screen)
		for i in range(2):
			if(Player_List[i].alived == 0 and Player_List[i].player_lives >= 1 ) :
				death_counter[0]+=1
				if(death_counter[0] > death_cooldown) :
					death_counter[0] = 0 
					Player_List[i].alived = 1 
					Player_List[i].reset(Player_Coord[i][0] , Player_Coord[i][1] , i)
			if(Player_List[i].alived == 1 and Player_List[i].player_lives >=1 ) :
				Player_List[i].update(Player_List[i].alived,Game_Screen , bomb_list , explosion_list , background_list , destrucable_list , undestrucalbe_list , item_list , i ,Player_List[i].player_lives)
		
		
		pygame.display.update()
