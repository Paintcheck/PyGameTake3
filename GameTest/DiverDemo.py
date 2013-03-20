import pygame
#this is a test of the please sync for god's sake
Ldiverdude = pygame.image.load("Lscubadiversmall.png")
Rdiverdude = pygame.image.load("Rscubadiversmall.png")

Ldiverbuddy = pygame.image.load("Lbuddy.png")
Rdiverbuddy = pygame.image.load("Rbuddy.png")

Reel = pygame.image.load("Reel.png")

Lcfishmedium = pygame.image.load("Lcfishmedium.png")

Lcfishsmall = pygame.image.load("Lcfishsmall.png")

treasuresmall = pygame.image.load("treasuresmall.png")

treasurebig = pygame.image.load("treasurebig.png")

AcquariumBackground = pygame.image.load("Aquarium.jpg")

ocean = [135, 206, 250] 
black = [0, 0, 0]
# Function to draw our stick figure
def LdrawDiver(screen,x,y):
    screen.blit(Ldiverdude, (x, y))
def RdrawDiver(screen,x,y):
    screen.blit(Rdiverdude, (x, y))  
    
def LdrawBuddy(screen,x,y):
    screen.blit(Ldiverbuddy, (x, y))
def RdrawBuddy(screen,x,y):
    screen.blit(Rdiverbuddy, (x, y))  

def Rdraweel(screen,x,y):
    screen.blit(Reel, (x, y))

def Ldrawcfishmedium(screen,x,y):
    screen.blit(Lcfishmedium, (x, y))
    
def Ldrawcfishsmall(screen,x,y):
    screen.blit(Lcfishsmall, (x, y))

def drawtreasuresmall(screen,x,y):
    screen.blit(treasuresmall, (x, y))
    
def drawtreasurebig(screen,x,y):
    screen.blit(treasurebig, (x, y))  
    
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
x_coord=0
y_coord=0

x_coordbuddy=0
y_coordbuddy=0

x_coordeel = -250
y_coordeel = 768 - 200

x_coordcfishmedium = 1024 + 250
y_coordcfishmedium = 200

x_coordcfishsmall = 1024 + 250 + 100
y_coordcfishsmall = 200 + 11

#Direction to face
direction = 1
buddydirection =1
speed=10

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
                x_speed=-speed
                direction=0
            if event.key == pygame.K_RIGHT:
                x_speed=speed
                direction=1
            if event.key == pygame.K_UP:
                y_speed=-speed
            if event.key == pygame.K_DOWN:
                y_speed=speed
                  
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
 
    if x_coord < 0:
        x_coord = 0
    if y_coord < 0:
        y_coord = 0
    if x_coord > 1024-224:
        x_coord = 1024-224
    if y_coord > 768-188:
        y_coord = 768-188
        
    if x_coord > x_coordbuddy + 224:
        buddydirection = 1
        x_coordbuddy = x_coord - 224
    if x_coord < x_coordbuddy - 224:
        buddydirection = 0
        x_coordbuddy = x_coord + 224
    if y_coord > y_coordbuddy + 188:
        y_coordbuddy = y_coord - 188
    if y_coord < y_coordbuddy - 188:
        y_coordbuddy = y_coord + 188            
            
            
    if x_coordbuddy < 0:
        x_coordbuddy = 0
    if y_coordbuddy < 0:
        y_coordbuddy = 0
    if x_coordbuddy > 1024-224:
        x_coordbuddy = 1024-224
    if y_coordbuddy > 768-188:
        y_coordbuddy = 768-188
        
    # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT    
 
    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
      
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(ocean)
    screen.blit(AcquariumBackground, (0,0))
    
    
    drawtreasuresmall(screen, 1024 - 120, 768 - 100)
    
    if buddydirection == 1:
            RdrawBuddy(screen, x_coordbuddy, y_coordbuddy)
    else:
        LdrawBuddy(screen, x_coordbuddy, y_coordbuddy)
        
    if direction == 1:
        RdrawDiver(screen, x_coord, y_coord)
    else:
        LdrawDiver(screen, x_coord, y_coord)
        
    x_coordeel = x_coordeel + 5
    if x_coordeel > 1024:
        x_coordeel = -500
    Rdraweel(screen, x_coordeel, y_coordeel)
    
    x_coordcfishmedium = x_coordcfishmedium - 2
    if x_coordcfishmedium < -100:
        x_coordcfishmedium = 1024 + 500
    Ldrawcfishmedium(screen, x_coordcfishmedium, y_coordcfishmedium)
    
    x_coordcfishsmall = x_coordcfishsmall - 2
    if x_coordcfishsmall < -100 + 100:
        x_coordcfishsmall = 1024 + 500 + 100
    Ldrawcfishsmall(screen, x_coordcfishsmall, y_coordcfishsmall)
 
    if x_coord == 1024 - 224 and y_coord == 768 - 188:
        drawtreasurebig(screen, 276, 187)
        
    
 
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
      
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
  
    # Limit to 30 frames per second
    clock.tick(30)
      
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE (indeed it will I found this out the hard way)
pygame.quit ()


