from List_Modunle import *
import Main_Menu_Window
from Profile import * 
from Boss import * 

def Run(Map_State) :
	Game_Screen = pygame.display.set_mode((Game_Window_Width, Game_Window_Height))
	Player_List = [Player(312 , 48 , 0) , Player(984 , 48 , 1) , Player(312 , 624 , 2) , Player(984 , 624 , 3)]
	Player_Coord = [(312 , 48) , (984 , 48) , (312 , 624) , (984 , 624)]
	
	
	
	portal_list = []
	storm_list = []
	bomb_list = []
	explosion_list = []
	destrucable_list = []
	undestrucable_list = []
	background_list = []
	item_list = []
	spawn_list = []
	# Set the caption of the screen
	pygame.display.set_caption('LABOOMXA')
	Profile_Now = Profile(Player_List)
	# Update the display using flip
	pygame.display.flip()
	  
	# Variable to keep our game loop running
	running = True	
	clock = pygame.time.Clock()
	Game_boss = Boss(595 , 288, Map_State)
	Board  = Play_Board(Map_State ,background_list , destrucable_list , undestrucable_list )
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
		Board.Draw_Board(Game_Screen ,background_list , destrucable_list , undestrucable_list ,portal_list , item_list )
		Profile_Now.draw(Game_Screen)
		ok = Game_boss.draw(Game_Screen)
		if ok :
			Board.GenerateSpawn(Game_Screen , background_list , item_list , spawn_list)
		
		render_item = False 
		for tile in spawn_list :
			if tile.is_render == True :
				render_item = True
		if render_item :
			Board.GenerateItem(Game_Screen , spawn_list , item_list)
			spawn_list.clear()
		for tile in spawn_list :
			tile.draw(Game_Screen)
		if len(explosion_list) > 0 :
				for t in explosion_list :
					if t.is_denotated() == True :
						explosion_list.remove(t)
		if len(bomb_list) > 0 :
			for t in bomb_list :
				if t[1] == 0:
					isWall = 1
					for i in range(4):
						if t[0].rect.colliderect(Player_List[i].rect):
							isWall = 0
					t[1] = isWall
				if t[0].draw(Game_Screen,background_list , destrucable_list , undestrucable_list , item_list) == True :
					bomb_list.remove(t)
		if len(item_list) > 0 :
			for t in item_list :
				t.draw(Game_Screen)
		if len(storm_list) > 0 :
			for t in storm_list :
				if t.draw(Game_Screen , destrucable_list , undestrucable_list ) == True :
					storm_list.remove(t)
		for i in range(4):
			if(Player_List[i].alived == 0 and Player_List[i].player_lives >= 1 ) :
				death_counter[0]+=1
				if(death_counter[0] > death_cooldown) :
					death_counter[0] = 0 
					Player_List[i].alived = 1 
					Player_List[i].reset(Player_Coord[i][0] , Player_Coord[i][1] , i)
			if(Player_List[i].alived == 1 and Player_List[i].player_lives >=1 ) :
				Player_List[i].update(Player_List[i].alived,Game_Screen , bomb_list , explosion_list , background_list , destrucable_list , undestrucable_list ,storm_list , portal_list , item_list , i ,Player_List[i].player_lives)
		
		
		pygame.display.update()