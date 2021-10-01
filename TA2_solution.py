import pygame
pygame.init() 
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
size=(600,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout Game")
paddle=pygame.Rect(300,500,60,10)
ball=pygame.Rect(200,250,10,10)
ballx=-1
bally=-1
carryOn = True
while carryOn:
    for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                  carryOn = False 
    screen.fill(DARKBLUE)
    
    pygame.draw.rect(screen,LIGHTBLUE,paddle)
    ball.x=ball.x+ballx
    ball.y=ball.y+bally

    #Create boundaries for x axis of movement
    if ball.x>=590:
      ballx=-ballx
    if ball.x<=10:
      ballx=-ballx


    pygame.draw.rect(screen,WHITE ,ball)
    pygame.time.wait(20)
    pygame.display.flip()
pygame.quit()
    
