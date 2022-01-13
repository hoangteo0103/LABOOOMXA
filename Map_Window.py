from List_Modunle import *
import Main_Menu_Window
import Game_Window

def Run() :
	pygame.time.delay(300)
	Map_Window_Width = 1080
	Map_Window_Height = 720
	Image_Width = 17 * 36
	Image_Height = 15 * 36
	Map_Image_List = [pygame.transform.scale(pygame.image.load(f'Game_Data/Image/Map_Image/Map{i}.png') , (Image_Width , Image_Height)) for i in range(1 , 2)]
	Map_Button_List = []
	for i in Map_Image_List:
		Map_Button_List.append(Button(Map_Window_Width // 2 - Image_Width // 2 , Map_Window_Height // 2 - Image_Height // 2 , i , 1))
		# Map_Screen.blit(i , (Map_Window_Width // 2 - Image_Width // 2 , Map_Window_Height // 2 - Image_Height // 2))
	Map_Screen = pygame.display.set_mode((Map_Window_Width, Map_Window_Height))
	running = True	
	pygame.display.set_caption('LABOOMXA')
	pygame.display.flip()
	while running:
		for event in pygame.event.get():
			# Check for QUIT event      
			if event.type == pygame.QUIT:
				running = False	
				Main_Menu_Window.Run()
				exit()

		for i in Map_Button_List:
			i.draw(Map_Screen)

		for i in range(1 , 2):
			if Map_Button_List[i - 1].isClicked(Map_Screen):
				Game_Window.Run(i)
				exit()
		
		pygame.display.update()