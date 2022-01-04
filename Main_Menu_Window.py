from List_Modunle import *
import Setting_Window
import Game_Window
Play_Game_Button = Button(280 , 150 , Play_Button_Image , 1)
Setting_Game_Button = Button(280 , 250 , Setting_Button_Image , 1)
Instruction_Game_Button = Button(280 , 350 , Instruction_Button_Image , 1)
Quit_Game_Button = Button(280 , 450 , Quit_Button_Image , 1)

def Run():
    Main_Menu_Screen = pygame.display.set_mode((Main_Menu_Window_Width, Main_Menu_Window_Height))

    # Set the caption of the screen
    pygame.display.set_caption('LABOOMXA')
      
    # Update the display using flip
    pygame.display.flip()
      
    # Variable to keep our game loop running
    running = True	
      
    # game loop
    while running:
        for event in pygame.event.get():
            # Check for QUIT event      
            if event.type == pygame.QUIT:
                running = False

        Main_Menu_Screen.blit(Main_Menu_Image, (0, 0))
        Play_Game_Button.draw(Main_Menu_Screen)
        Setting_Game_Button.draw(Main_Menu_Screen)
        Instruction_Game_Button.draw(Main_Menu_Screen)
        Quit_Game_Button.draw(Main_Menu_Screen)

        if(Play_Game_Button.isClicked(Main_Menu_Screen) == True):
        	Game_Window.Run() 
        if(Setting_Game_Button.isClicked(Main_Menu_Screen) == True):
            Setting_Window.Run()
        if(Quit_Game_Button.isClicked(Main_Menu_Screen) == True):
            running = False
        pygame.display.update()