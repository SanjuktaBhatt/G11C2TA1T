# Importing pygame library
import pygame
# Initialzing pygame
pygame.init() 
# Creating a game screen with width=600 and height=600
screen = pygame.display.set_mode((600,600))
# Setting the title of the game screen to "Breakout Game" 
pygame.display.set_caption("Breakout Game")
# Creating a paddle and a ball rectangle objects
paddle = pygame.Rect(300,500,60,10)
ball = pygame.Rect(200,250,10,10)

# Create variables "ballx" and "bally" and assign the value 1 to both



# Game loop
carryOn = True
while carryOn:
    for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # # Checking if user clicked on close on game screen
                  carryOn = False # Flag that we are done so we exit this loop  
    # Filling the screen with darkblue color. RGB combination for darkblue is (36,90,190)                
    screen.fill((36,90,190))
    # Drawing the lightblue colored paddle on screen. RGB combination for lightblue is (0,176,240)
    pygame.draw.rect(screen,(0,176,240),paddle)
    
    # Update varaibles "ballx" and "bally" to update the position of the ball
    
    
    
    # Limit ball movement on screen along x-axis
    
    
    
    
    # Limit ball movement on screen along y-axis 
    
    
    
    
    
    
    # Drawing the white colored ball on screen. RGB combination for white is (255,255,255)  
    pygame.draw.rect(screen,(255,255,255) ,ball)
    # Updating x and y positions of the ball every 20 seconds.    
    pygame.time.wait(20) # Adding this will enable us to monitor the speed with which ball moves.
    # Updating the contents of entire display
    pygame.display.flip()
# Quit the game    
pygame.quit()
