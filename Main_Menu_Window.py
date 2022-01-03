from List_Modunle import *

# Define the background colour
# using RGB color coding
background_colour = (234, 212, 252)
  
# Define the dimensions of
# screen object(width,height)
screen = pygame.display.set_mode((Main_Menu_Window_Width, Main_Menu_Window_Height))
  
# Set the caption of the screen
pygame.display.set_caption('LABOOMXA')
  
# Fill the background colour to the screen
screen.fill(background_colour)
  
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

    screen.blit(Main_Menu_Image, (0, 0))
    pygame.display.update()

#Start_Game_Window()

#Setting_Window()

#Instruction()

#Quit_Window()