import pygame

Ldiverdude = pygame.image.load("Lscubadiversmall.gif")
Rdiverdude = pygame.image.load("Rscubadiversmall.gif")

ocean = [135, 206, 250] 
black = [0, 0, 0]
# Function to draw our stick figure
def LdrawDiver(screen,x,y):
    Ldiverdude = pygame.image.load("Lscubadiversmall.gif")
    screen.blit(Ldiverdude, (x, y))
def RdrawDiver(screen,x,y):
    Ldiverdude = pygame.image.load("Rscubadiversmall.gif")
    screen.blit(Rdiverdude, (x, y))     
# Setup
pygame.init()
   
# Set the width and height of the screen [width,height]
size=[1024,768]
screen=pygame.display.set_mode(size)
  
pygame.display.set_caption("Diver Test")
  
#Loop until the user clicks the close button.
done=False
  
# Used to manage how fast the screen updates
clock=pygame.time.Clock()
 
# Hide the mouse cursor
pygame.mouse.set_visible(0)
 
# Speed in pixels per frame
x_speed=0
y_speed=0
  
# Current position
x_coord=10
y_coord=10

#Direction to face
direction=1
# -------- Main Program Loop -----------
while done==False:
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
            # User pressed down on a key
         
        if event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                x_speed=-3
                direction=0
            if event.key == pygame.K_RIGHT:
                x_speed=3
                direction=1
            if event.key == pygame.K_UP:
                y_speed=-3
            if event.key == pygame.K_DOWN:
                y_speed=3
                  
        # User let up on a key
        if event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT:
                x_speed=0
            if event.key == pygame.K_RIGHT:
                x_speed=0
            if event.key == pygame.K_UP:
                y_speed=0
            if event.key == pygame.K_DOWN:
                y_speed=0
    # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
 
    # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
 
    # Move the object according to the speed vector.
    x_coord=x_coord+x_speed
    y_coord=y_coord+y_speed
 
    # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT    
 
    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
      
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(ocean)
    
    if direction == 1:
        RdrawDiver(screen,x_coord,y_coord)
    else:
        LdrawDiver(screen,x_coord,y_coord)

     
 
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
      
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
  
    # Limit to 30 frames per second
    clock.tick(30)
      
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE (indeed it will I found this out the hard way)
pygame.quit ()


