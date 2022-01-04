from List_Modunle import *
import Setting_Window
import Game_Window
Start_Game_Button = Button(250  , 150 , Start_Button_Image , 1)
Option_Game_Button = Button(250  , 250 , Option_Button_Image , 1)
Exit_Game_Button = Button(250  , 350 , Exit_Button_Image , 1)

def Main_Menu_Window():
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
        Start_Game_Button.draw(Main_Menu_Screen)
        Option_Game_Button.draw(Main_Menu_Screen)
        Exit_Game_Button.draw(Main_Menu_Screen)

        if(Start_Game_Button.isClicked(Main_Menu_Screen) == True):
        	Game_Window.run() 
        if(Option_Game_Button.isClicked(Main_Menu_Screen) == True):
            Setting_Window.Setting_Window()
            exit()
        if(Exit_Game_Button.isClicked(Main_Menu_Screen) == True):
            exit()

        pygame.display.update()