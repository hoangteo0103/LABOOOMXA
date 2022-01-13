from List_Modunle import *
import Setting_Window
import Game_Window
import Map_Window
import Quit_Window
Play_Game_Button = Button(280 , 200 , Play_Button_Image , 1)
Setting_Game_Button = Button(280 , 320 , Setting_Button_Image , 1)
Instruction_Game_Button = Button(280 , 440 , Instruction_Button_Image , 1)
Quit_Game_Button = Button(280 , 560 , Quit_Button_Image , 1)

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
            Map_Window.Run()
        if(Setting_Game_Button.isClicked(Main_Menu_Screen) == True):
            Setting_Window.Run()
        if(Quit_Game_Button.isClicked(Main_Menu_Screen) == True):
            Running = False
            Quit_Window.Quit_Window()
        pygame.display.update()
