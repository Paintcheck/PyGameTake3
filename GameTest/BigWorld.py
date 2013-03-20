import pygame
import time
#this is a test of the please sync for god's sake
map = pygame.image.load("TreasureMap.jpg") # 224 x 188

Ldiverdude = pygame.image.load("Lscubadiversmall.png") # 224 x 188
Rdiverdude = pygame.image.load("Rscubadiversmall.png") # 224 x 188

Ldiverbuddy = pygame.image.load("Lbuddy.png") # 224 x 188
Rdiverbuddy = pygame.image.load("Rbuddy.png") # 224 x 188

Reel = pygame.image.load("Reel.png") # 200 x 46
eel = pygame.image.load("eel.png") # 538 x 125

Lcfishmedium = pygame.image.load("Lcfishmedium.png") # 100 x 45
Lcfishsmall = pygame.image.load("Lcfishsmall.png") # 50 x 22
cfish = pygame.image.load("cfish.png") # 476 x 212

treasuresmall = pygame.image.load("treasuresmall.png") # 120 x 100

rocks = pygame.image.load("rocks.gif") # 200 x 768

treasurebig = pygame.image.load("treasurebig.png") # 472 x 395

seafloor = pygame.image.load("seafloor2.jpg") # 6000 x 768

AquariumBackground = pygame.image.load("Aquarium.jpg")

speed = 10
eelspeed = 5
cfishspeed = 2

spacehit = False

ocean = [135, 206, 250] 
black = [0, 0, 0]
# Function to draw our stick figure
def drawmap(screen,x,y):
    screen.blit(map, (x, y))

def drawseafloor(screen,x,y):
    screen.blit(seafloor, (x, y))

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

def draweel(screen,x,y):
    screen.blit(eel, (x, y))
    
def Ldrawcfishmedium(screen,x,y):
    screen.blit(Lcfishmedium, (x, y))
    
def Ldrawcfishsmall(screen,x,y):
    screen.blit(Lcfishsmall, (x, y))

def drawcfish(screen,x,y):
    screen.blit(cfish, (x, y))
    
def drawtreasuresmall(screen,x,y):
    screen.blit(treasuresmall, (x, y))
    
def drawtreasurebig(screen,x,y):
    screen.blit(treasurebig, (x, y))

def drawrocks(screen,x,y):
    screen.blit(rocks, (x, y))
    
def collision(object1, object2):
    x1 = object1[0]
    y1 = object1[1]
    dimx1 = object1[2]
    dimy1 = object1[3]
    x2 = object2[0]
    y2 = object2[1]
    dimx2 = object2[2]
    dimy2 = object2[3]
    if (x1 > x2 and x1 < x2 + dimx2 and y1 > y2 and y1 < y2 + dimy2) or (x1 + dimx1 > x2 and x1 + dimx1 < x2 + dimx2 and y1 > y2 and y1 < y2 + dimy2) or (x1 + dimx1 > x2 and x1 + dimx1 < x2 + dimx2 and y1 + dimy1 > y2 and y1 + dimy1 < y2 + dimy2) or (x1 > x2 and x1 < x2 + dimx2 and y1 + dimy1 > y2 and y1 + dimy1 < y2 + dimy2) or (x2 > x1 and x2 < x1 + dimx1 and y2 > y1 and y2 < y1 + dimx1) or (x2 + dimx2 > x1 and x2 + dimx2 < x1 + dimx1 and y2 > y1 and y2 < y1 + dimy1) or (x2 + dimx2 > x1 and x2 + dimx2 < x1 + dimx1 and y2 + dimy2 > y1 and y2 + dimy2 < y1 + dimy1) or (x2 > x1 and x2 < x1 + dimx1 and y2 + dimy2 > y1 and y2 + dimy2 < y1 + dimy1):
        return True
    else:
        return False
    
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
x_coord=449
y_coord=0

x_coordbuddy=0
y_coordbuddy=0

x_coordeel = -250
y_coordeel = 768 - 200

x_coordcfishmedium = 1024 + 250
y_coordcfishmedium = 200

x_coordcfishsmall = 1024 + 250 + 100
y_coordcfishsmall = 200 + 11

x_coordtreasure = 3000
y_coordtreasure = 768 - 100
treasure_c = [x_coordtreasure, y_coordtreasure, 120, 100]

x_coordback = 0 - 500
y_coordback = 0

#Direction to face
direction = 1
buddydirection =1
page = 0

# -------- Main Program Loop -----------
while done==False:


################# Map Page 0 ###########################
    if page == 0:
        drawmap(screen, 0, 0)
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done=True # Flag that we are done so we exit this loop
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    page = 1
########################################################

################# Page 1 ###############################
    elif page == 1:
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
                if event.key == pygame.K_SPACE:
                    spacehit = True
                      
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
                if event.key == pygame.K_SPACE:
                    spacehit = False
                
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
        screen.blit(AquariumBackground, (0,0))
        
        
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
            if spacehit == True:
                page = 2



########################################################

################# Page 2 ###############################
    elif page == 2:
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
                if event.key == pygame.K_SPACE:
                    spacehit = True
                      
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
                if event.key == pygame.K_SPACE:
                    spacehit = False
        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
     
        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
     
        # Move the object according to the speed vector.
        x_coord=x_coord+x_speed
        y_coord=y_coord+y_speed
     
        if x_coord < 0:
            x_coord = 0
            x_coordback = x_coordback + speed
            if x_coordback > 0:
                x_coordback = 0
            else:
                x_coordeel = x_coordeel + speed
                x_coordcfishmedium = x_coordcfishmedium + speed
                x_coordcfishsmall = x_coordcfishsmall + speed
                x_coordtreasure = x_coordtreasure + speed
        if y_coord < 0:
            y_coord = 0
        if x_coord > 1024-224:
            x_coord = 1024-224
            x_coordback = x_coordback - speed
            if x_coordback < -6000 + 1024:
                x_coordback = -6000 + 1024
            else:
                x_coordeel = x_coordeel - speed
                x_coordcfishmedium = x_coordcfishmedium - speed
                x_coordcfishsmall = x_coordcfishsmall - speed
                x_coordtreasure = x_coordtreasure - speed
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
        #screen.blit(SeafloorBackground, (0,0))
        
        drawseafloor(screen, x_coordback, y_coordback)
        drawrocks(screen, x_coordback - 100, 0)
        drawrocks(screen, x_coordback + 100 + 6000 - 200, 0)
        drawtreasuresmall(screen, x_coordtreasure, y_coordtreasure)
        
        if buddydirection == 1:
                RdrawBuddy(screen, x_coordbuddy, y_coordbuddy)
        else:
            LdrawBuddy(screen, x_coordbuddy, y_coordbuddy)
            
        if direction == 1:
            RdrawDiver(screen, x_coord, y_coord)
        else:
            LdrawDiver(screen, x_coord, y_coord)
            
        x_coordeel = x_coordeel + eelspeed
        if x_coordeel > x_coordback + 6000:
            x_coordeel = x_coordback - 200
        Rdraweel(screen, x_coordeel, y_coordeel)
        
        x_coordcfishmedium = x_coordcfishmedium - cfishspeed
        if x_coordcfishmedium < x_coordback - 100 - 50:
            x_coordcfishmedium = x_coordback + 6000
        Ldrawcfishmedium(screen, x_coordcfishmedium, y_coordcfishmedium)
        
        x_coordcfishsmall = x_coordcfishsmall - cfishspeed
        if x_coordcfishsmall < x_coordback - 100 - 50 + 100:
            x_coordcfishsmall = x_coordback + 6000 + 100
        Ldrawcfishsmall(screen, x_coordcfishsmall, y_coordcfishsmall)
     
        player_c = [x_coord, y_coord, 224, 188]
        buddy_c = [x_coordbuddy, y_coordbuddy, 224, 188]
        eel_c = [x_coordeel, y_coordeel, 200, 46]
        treasure_c = [x_coordtreasure, y_coordtreasure, 120, 100]
        cfishmedium_c = [x_coordcfishmedium, y_coordcfishmedium, 100, 45]
        
        if collision(player_c, treasure_c):
            drawtreasurebig(screen, 276, 187)
        if collision(player_c, eel_c):
            draweel(screen, 243, 322)
        if collision(player_c, cfishmedium_c):
            drawcfish(screen, 274, 278)
########################################################
     
       
        
        
        
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
      
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
  
    # Limit to 30 frames per second
    clock.tick(30)
      
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE (indeed it will I found this out the hard way)
pygame.quit ()


