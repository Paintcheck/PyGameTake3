import pygame
import sys
import time
import csv
# Setup
pygame.init() #Moved this up here because it was messing with stuff. No reason for it to come after all these anyway
pygame.time.set_timer(pygame.USEREVENT+1, 5000)

def load(savefile):
    with open(savefile, 'rt') as f:
        reader = csv.reader(f)
        save = list(reader)
        loadsavetext = save[0], save[2], save[4]
        return loadsavetext

def save(newsavearray):
    writer = csv.writer(open('Save1.csv', 'w'), delimiter=' ')
    writer.writeheader
    writer.writerow([newsavearray[0]])
    writer.writerow([newsavearray[1]])
    writer.writerow([newsavearray[2]])
    writer.writeheader
# How to save a new file
#newsave = 'Dennis', '5', '200'
#save(newsave)

# How to load a saved file
loadsavetext = load('Save1.csv')




Name = str(loadsavetext[0]).replace("[", "").replace("'","").replace("]","")
Level = map(int, loadsavetext[1])
Money = map(int, loadsavetext[2])

#finally:
 #   f.close()
#this is a test of the please sync for god's sake
map = pygame.image.load("TreasureMap.jpg") # 224 x 188

Ldiverdude = pygame.image.load("Lscubadiversmall.png") # 224 x 188
Rdiverdude = pygame.image.load("Rscubadiversmall.png") # 224 x 188

Ldiverbuddy = pygame.image.load("Lbuddy.png") # 224 x 188
Rdiverbuddy = pygame.transform.flip(Ldiverbuddy, True, False)

Reel = pygame.image.load("Reel.png") # 200 x 46
eel = pygame.image.load("eel.png") # 538 x 125

Lcfishmedium = pygame.image.load("Lcfishmedium.png") # 100 x 45
Lcfishsmall = pygame.image.load("Lcfishsmall.png") # 50 x 22
cfish = pygame.image.load("cfish.png") # 476 x 212

treasuresmall = pygame.image.load("treasuresmall.png") # 120 x 100

rocks = pygame.image.load("rocks.gif") # 200 x 768

treasurebig = pygame.image.load("treasurebig.png") # 472 x 395

seafloor = pygame.image.load("seafloor.jpg") # 6000 x 768

sandcastle = pygame.image.load("sandcastle.png") # 6000 x 768

bubbles = pygame.image.load("bubblessmall.gif") # 25 x 51

island = pygame.image.load("island.png") # 50 x 50

menu = pygame.image.load("MenuButton.png") # 100 x 50

AquariumBackground = pygame.image.load("Aquarium.jpg") # 1024 x 768

bubblespeed = 2
speed = 10
eelspeed = 5
cfishspeed = 2

#############Air Vars go Here###############
airgauge = pygame.image.load("AirGauge.png")

air_consumption = 1 
total_air = 100
font = pygame.font.Font(None, 30) #Debugging air consumption cod
##############################################
spacehit = False

ocean = [135, 206, 250] 
black = [0, 0, 0]
# Function to draw our stick figure
def drawmap(screen,x,y):
    screen.blit(map, (x, y))

def drawseafloor(screen,x,y):
    screen.blit(seafloor, (x, y))
    
def drawsandcastle(screen,x,y):
    screen.blit(sandcastle, (x, y))
    
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

def drawbubbles(screen,x,y):
    screen.blit(bubbles, (x, y))
    
def drawisland(screen,x,y):
    screen.blit(island, (x, y))   
    
def drawmenu(screen,x,y):
    screen.blit(menu, (x, y))   
     
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
    
def drawgauge(screen, x, y):
    screen.blit(airgauge, (x, y))


    
# Set the width and height of the screen [width,height]
size=[1024,768]
screen=pygame.display.set_mode(size)
  
pygame.display.set_caption("Diver Test - " + Name)
  
#Loop until the user clicks the close button.
done=False
  
# Used to manage how fast the screen updates
clock=pygame.time.Clock()
 
# Hide the mouse cursor
pygame.mouse.set_visible(1)


x_menu = 0
y_menu = 0
# Speed in pixels per frame
x_speed = 0
y_speed = 0
  
# Current position
x_coord = 449
y_coord = 0

x_coordbuddy = 0
y_coordbuddy = 0

x_coordbubbles1 = 0
y_coordbubbles1 = 0
x_coordbubbles2 = 0
y_coordbubbles2 = 0
x_coordbubbles3 = 0
y_coordbubbles3 = 0
x_coordbubbles4 = 0
y_coordbubbles4 = 0

x_b_coordbubbles1 = 0
y_b_coordbubbles1 = 0
x_b_coordbubbles2 = 0
y_b_coordbubbles2 = 0
x_b_coordbubbles3 = 0
y_b_coordbubbles3 = 0
x_b_coordbubbles4 = 0
y_b_coordbubbles4 = 0

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

x_coordgauge = screen.get_width() - airgauge.get_width()
y_coordgauge = 0

#Direction to face
bubblecycles1 = 0
bubblecycles2 = 0
bubblecycles3 = 0
bubblecycles4 = 0

b_bubblecycles1 = 0
b_bubblecycles2 = 0
b_bubblecycles3 = 0
b_bubblecycles4 = 0

direction = 1
buddydirection =1
page = 0


# -------- Main Program Loop -----------
while done==False:
    # Limit to 30 frames per second
    clock.tick(30)


################# Map Level 0 ###########################
    if page == 0:
        drawmap(screen, 0, 0)
        x_outer_banks = 220
        y_outer_banks = 280
        drawisland(screen, x_outer_banks, y_outer_banks)
        x_singapore = 750
        y_singapore = 385
        drawisland(screen, x_singapore, y_singapore)
        mouse_pos = pygame.mouse.get_pos()
        x_mouse = mouse_pos[0]
        y_mouse = mouse_pos[1]
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done=True # Flag that we are done so we exit this loop
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                if x_mouse > x_singapore and x_mouse < x_singapore + 50 and y_mouse > y_singapore and y_mouse < y_singapore + 50:
                    page = 1
                if x_mouse > x_outer_banks and x_mouse < x_outer_banks + 50 and y_mouse > y_outer_banks and y_mouse < y_outer_banks + 50:
                    page = 2
#########################################################

################# Level 1 ###############################
    elif page == 1:
        mouse_pos = pygame.mouse.get_pos()
        x_mouse = mouse_pos[0]
        y_mouse = mouse_pos[1]
        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        for event in pygame.event.get(): # User did something
            if event.type == pygame.USEREVENT+1:
                total_air-=air_consumption
                #print("Consume Air Called")
            if event.type == pygame.QUIT: # If user clicked close
                done=True # Flag that we are done so we exit this loop
                # User pressed down on a key
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                if x_mouse > x_menu and x_mouse < x_menu + 100 and y_mouse > y_menu and y_mouse < y_menu + 50:
                    page = 0   
            if event.type == pygame.KEYDOWN:
                
                # Figure out if it was an arrow key. If so
                # adjust speed.
                if event.key == pygame.K_a:
                    x_speed=-speed
                    direction=0
                    air_consumption = 2 #More air used while swimming
                if event.key == pygame.K_d:
                    x_speed=speed
                    direction=1
                    air_consumption = 2 #More air used while swimming
                if event.key == pygame.K_w:
                    y_speed=-speed
                    air_consumption = 2 #More air used while swimming
                if event.key == pygame.K_s:
                    y_speed=speed
                    air_consumption = 2 #More air used while swimming
                if event.key == pygame.K_SPACE:
                    spacehit = True
                if event.key == pygame.K_ESCAPE:
                    page = 0
                      
            # User let up on a key
            if event.type == pygame.KEYUP:
                air_consumption = 1
                # If it is an arrow key, reset vector back to zero
                if event.key == pygame.K_a:
                    x_speed=0
                if event.key == pygame.K_d:
                    x_speed=0
                if event.key == pygame.K_w:
                    y_speed=0
                if event.key == pygame.K_s:
                    y_speed=0
                if event.key == pygame.K_SPACE:
                    spacehit = False
        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
     
        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
     
        # Move the object according to the speed vector.
        
        x_coord = x_coord + x_speed
        y_coord = y_coord + y_speed
        
        xstep = 20
        ystep = 20
        #bubbles
        if bubblecycles1 == 0:
            if direction == 0:
                x_coordbubbles1 = x_coord + 55
                y_coordbubbles1 = y_coord + 60 - 51
            else:
                x_coordbubbles1 = x_coord - 55 + 224
                y_coordbubbles1 = y_coord + 60 - 51
        bubblecycles1 = bubblecycles1 + 1
        if bubblecycles1 > 360:
            bubblecycles1 = 0
        y_coordbubbles1 = y_coordbubbles1 - bubblespeed

        if bubblecycles2 == 90:
            if direction == 0:
                x_coordbubbles2 = x_coord + 55
                y_coordbubbles2 = y_coord + 60 - 51
            else:
                x_coordbubbles2 = x_coord - 55 + 224
                y_coordbubbles2 = y_coord + 60 - 51
        bubblecycles2 = bubblecycles2 + 1
        if bubblecycles2 > 455:
            bubblecycles2 = 90
        y_coordbubbles2 = y_coordbubbles2 - bubblespeed

        if bubblecycles3 == 180:
            if direction == 0:
                x_coordbubbles3 = x_coord + 55
                y_coordbubbles3 = y_coord + 60 - 51
            else:
                x_coordbubbles3 = x_coord - 55 + 224
                y_coordbubbles3 = y_coord + 60 - 51
        bubblecycles3 = bubblecycles3 + 1
        if bubblecycles3 > 540:
            bubblecycles3 = 180
        y_coordbubbles3 = y_coordbubbles3 - bubblespeed        

        if bubblecycles4 == 270:
            if direction == 0:
                x_coordbubbles4 = x_coord + 55
                y_coordbubbles4 = y_coord + 60 - 51
            else:
                x_coordbubbles4 = x_coord - 55 + 224
                y_coordbubbles4 = y_coord + 60 - 51
        bubblecycles4 = bubblecycles4 + 1
        if bubblecycles4 > 630:
            bubblecycles4 = 270
        y_coordbubbles4 = y_coordbubbles4 - bubblespeed         

                
        
        
        offstep = 40
        
        if b_bubblecycles1 == 0 + offstep:
            if direction == 0:
                x_b_coordbubbles1 = x_coordbuddy + 55 
                y_b_coordbubbles1 = y_coordbuddy + 60 - 51
            else:
                x_b_coordbubbles1 = x_coordbuddy - 55  + 224
                y_b_coordbubbles1 = y_coordbuddy + 60 - 51
        b_bubblecycles1 = b_bubblecycles1 + 1
        if b_bubblecycles1 > 360 + offstep:
            b_bubblecycles1 = 0 + offstep
        y_b_coordbubbles1 = y_b_coordbubbles1 - bubblespeed

        if b_bubblecycles2 == 90 + offstep:
            if direction == 0:
                x_b_coordbubbles2 = x_coordbuddy + 55 
                y_b_coordbubbles2 = y_coordbuddy + 60 - 51
            else:
                x_b_coordbubbles2 = x_coordbuddy - 55  + 224
                y_b_coordbubbles2 = y_coordbuddy + 60 - 51
        b_bubblecycles2 = b_bubblecycles2 + 1
        if b_bubblecycles2 > 450 + offstep:
            b_bubblecycles2 = 90 + offstep
        y_b_coordbubbles2 = y_b_coordbubbles2 - bubblespeed

        if b_bubblecycles3 == 180 + offstep:
            if direction == 0:
                x_b_coordbubbles3 = x_coordbuddy + 55 
                y_b_coordbubbles3 = y_coordbuddy + 60 - 51
            else:
                x_b_coordbubbles3 = x_coordbuddy - 55  + 224
                y_b_coordbubbles3 = y_coordbuddy + 60 - 51
        b_bubblecycles3 = b_bubblecycles3 + 1
        if b_bubblecycles3 > 540 + offstep:
            b_bubblecycles3 = 180 + offstep
        y_b_coordbubbles3 = y_b_coordbubbles3 - bubblespeed        

        if b_bubblecycles4 == 270 + offstep:
            if direction == 0:
                x_b_coordbubbles4 = x_coordbuddy + 55 
                y_b_coordbubbles4 = y_coordbuddy + 60 - 51
            else:
                x_b_coordbubbles4 = x_coordbuddy - 55  + 224
                y_b_coordbubbles4 = y_coordbuddy + 60 - 51
        b_bubblecycles4 = b_bubblecycles4 + 1
        if b_bubblecycles4 > 630 + offstep:
            b_bubblecycles4 = 270 + offstep
        y_b_coordbubbles4 = y_b_coordbubbles4 - bubblespeed     
        
        
        
        
     
                
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
                
                x_coordbubbles1 = x_coordbubbles1 + speed
                x_coordbubbles2 = x_coordbubbles2 + speed
                x_coordbubbles3 = x_coordbubbles3 + speed
                x_coordbubbles4 = x_coordbubbles4 + speed
                
                x_b_coordbubbles1 = x_b_coordbubbles1 + speed
                x_b_coordbubbles2 = x_b_coordbubbles2 + speed
                x_b_coordbubbles3 = x_b_coordbubbles3 + speed
                x_b_coordbubbles4 = x_b_coordbubbles4 + speed
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
                
                x_coordbubbles1 = x_coordbubbles1 - speed
                x_coordbubbles2 = x_coordbubbles2 - speed
                x_coordbubbles3 = x_coordbubbles3 - speed
                x_coordbubbles4 = x_coordbubbles4 - speed
                
                x_b_coordbubbles1 = x_b_coordbubbles1 - speed
                x_b_coordbubbles2 = x_b_coordbubbles2 - speed
                x_b_coordbubbles3 = x_b_coordbubbles3 - speed
                x_b_coordbubbles4 = x_b_coordbubbles4 - speed
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
        drawsandcastle(screen, x_coordback, y_coordback)
        drawrocks(screen, x_coordback - 100, 0)
        drawrocks(screen, x_coordback + 100 + 6000 - 200, 0)
        drawtreasuresmall(screen, x_coordtreasure, y_coordtreasure)
        ####
        drawgauge(screen, x_coordgauge, y_coordgauge) #This way the air gauge is always in the background  
        ta = "Total air:" + str(total_air)
        airtext = font.render(ta, 1, black)
        screen.blit(airtext, (x_coordgauge, y_coordgauge))
        ##AirGauge##
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
        
        drawbubbles(screen, x_coordbubbles1, y_coordbubbles1)
        drawbubbles(screen, x_coordbubbles2, y_coordbubbles2)
        drawbubbles(screen, x_coordbubbles3, y_coordbubbles3)
        drawbubbles(screen, x_coordbubbles4, y_coordbubbles4)
     
        drawbubbles(screen, x_b_coordbubbles1, y_b_coordbubbles1)
        drawbubbles(screen, x_b_coordbubbles2, y_b_coordbubbles2)
        drawbubbles(screen, x_b_coordbubbles3, y_b_coordbubbles3)
        drawbubbles(screen, x_b_coordbubbles4, y_b_coordbubbles4)
        
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
        
        drawmenu(screen, x_menu, y_menu)
       
########################################################

################# Level 2 ###############################
    elif page == 2:
        mouse_pos = pygame.mouse.get_pos()
        x_mouse = mouse_pos[0]
        y_mouse = mouse_pos[1]
      
       #All event processing goes below this comment
        for event in pygame.event.get(): # User did something
            if event.type == pygame.USEREVENT+1:
                total_air-=air_consumption
                #print("Consume Air Called")
            if event.type == pygame.QUIT: # If user clicked close
                done=True # Flag that we are done so we exit this loop
                # User pressed down on a key
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                if x_mouse > x_menu and x_mouse < x_menu + 100 and y_mouse > y_menu and y_mouse < y_menu + 50:
                    page = 0   
            if event.type == pygame.KEYDOWN:
                
                # Figure out if it was an arrow key. If so
                # adjust speed.
                if event.key == pygame.K_a:
                    x_speed=-speed
                    direction=0
                    air_consumption = 2 #More air used while swimming
                if event.key == pygame.K_d:
                    x_speed=speed
                    direction=1
                    air_consumption = 2 #More air used while swimming
                if event.key == pygame.K_w:
                    y_speed=-speed
                    air_consumption = 2 #More air used while swimming
                if event.key == pygame.K_s:
                    y_speed=speed
                    air_consumption = 2 #More air used while swimming
                if event.key == pygame.K_SPACE:
                    spacehit = True
                if event.key == pygame.K_ESCAPE:
                    page = 0
                      
            # User let up on a key
            if event.type == pygame.KEYUP:
                air_consumption = 1
                # If it is an arrow key, reset vector back to zero
                if event.key == pygame.K_a:
                    x_speed=0
                if event.key == pygame.K_d:
                    x_speed=0
                if event.key == pygame.K_w:
                    y_speed=0
                if event.key == pygame.K_s:
                    y_speed=0
                if event.key == pygame.K_SPACE:
                    spacehit = False
        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
     
        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
     
        # Move the object according to the speed vector.
        
        x_coord = x_coord + x_speed
        y_coord = y_coord + y_speed
        
        xstep = 20
        ystep = 20
        #bubbles
        if bubblecycles1 == 0:
            if direction == 0:
                x_coordbubbles1 = x_coord + 55
                y_coordbubbles1 = y_coord + 60 - 51
            else:
                x_coordbubbles1 = x_coord - 55 + 224
                y_coordbubbles1 = y_coord + 60 - 51
        bubblecycles1 = bubblecycles1 + 1
        if bubblecycles1 > 360:
            bubblecycles1 = 0
        y_coordbubbles1 = y_coordbubbles1 - bubblespeed

        if bubblecycles2 == 90:
            if direction == 0:
                x_coordbubbles2 = x_coord + 55
                y_coordbubbles2 = y_coord + 60 - 51
            else:
                x_coordbubbles2 = x_coord - 55 + 224
                y_coordbubbles2 = y_coord + 60 - 51
        bubblecycles2 = bubblecycles2 + 1
        if bubblecycles2 > 455:
            bubblecycles2 = 90
        y_coordbubbles2 = y_coordbubbles2 - bubblespeed

        if bubblecycles3 == 180:
            if direction == 0:
                x_coordbubbles3 = x_coord + 55
                y_coordbubbles3 = y_coord + 60 - 51
            else:
                x_coordbubbles3 = x_coord - 55 + 224
                y_coordbubbles3 = y_coord + 60 - 51
        bubblecycles3 = bubblecycles3 + 1
        if bubblecycles3 > 540:
            bubblecycles3 = 180
        y_coordbubbles3 = y_coordbubbles3 - bubblespeed        

        if bubblecycles4 == 270:
            if direction == 0:
                x_coordbubbles4 = x_coord + 55
                y_coordbubbles4 = y_coord + 60 - 51
            else:
                x_coordbubbles4 = x_coord - 55 + 224
                y_coordbubbles4 = y_coord + 60 - 51
        bubblecycles4 = bubblecycles4 + 1
        if bubblecycles4 > 630:
            bubblecycles4 = 270
        y_coordbubbles4 = y_coordbubbles4 - bubblespeed         

                
        
        
        offstep = 40
        
        if b_bubblecycles1 == 0 + offstep:
            if direction == 0:
                x_b_coordbubbles1 = x_coordbuddy + 55 
                y_b_coordbubbles1 = y_coordbuddy + 60 - 51
            else:
                x_b_coordbubbles1 = x_coordbuddy - 55  + 224
                y_b_coordbubbles1 = y_coordbuddy + 60 - 51
        b_bubblecycles1 = b_bubblecycles1 + 1
        if b_bubblecycles1 > 360 + offstep:
            b_bubblecycles1 = 0 + offstep
        y_b_coordbubbles1 = y_b_coordbubbles1 - bubblespeed

        if b_bubblecycles2 == 90 + offstep:
            if direction == 0:
                x_b_coordbubbles2 = x_coordbuddy + 55 
                y_b_coordbubbles2 = y_coordbuddy + 60 - 51
            else:
                x_b_coordbubbles2 = x_coordbuddy - 55  + 224
                y_b_coordbubbles2 = y_coordbuddy + 60 - 51
        b_bubblecycles2 = b_bubblecycles2 + 1
        if b_bubblecycles2 > 450 + offstep:
            b_bubblecycles2 = 90 + offstep
        y_b_coordbubbles2 = y_b_coordbubbles2 - bubblespeed

        if b_bubblecycles3 == 180 + offstep:
            if direction == 0:
                x_b_coordbubbles3 = x_coordbuddy + 55 
                y_b_coordbubbles3 = y_coordbuddy + 60 - 51
            else:
                x_b_coordbubbles3 = x_coordbuddy - 55  + 224
                y_b_coordbubbles3 = y_coordbuddy + 60 - 51
        b_bubblecycles3 = b_bubblecycles3 + 1
        if b_bubblecycles3 > 540 + offstep:
            b_bubblecycles3 = 180 + offstep
        y_b_coordbubbles3 = y_b_coordbubbles3 - bubblespeed        

        if b_bubblecycles4 == 270 + offstep:
            if direction == 0:
                x_b_coordbubbles4 = x_coordbuddy + 55 
                y_b_coordbubbles4 = y_coordbuddy + 60 - 51
            else:
                x_b_coordbubbles4 = x_coordbuddy - 55  + 224
                y_b_coordbubbles4 = y_coordbuddy + 60 - 51
        b_bubblecycles4 = b_bubblecycles4 + 1
        if b_bubblecycles4 > 630 + offstep:
            b_bubblecycles4 = 270 + offstep
        y_b_coordbubbles4 = y_b_coordbubbles4 - bubblespeed     
        
        
        
        
     
                
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
                
                x_coordbubbles1 = x_coordbubbles1 + speed
                x_coordbubbles2 = x_coordbubbles2 + speed
                x_coordbubbles3 = x_coordbubbles3 + speed
                x_coordbubbles4 = x_coordbubbles4 + speed
                
                x_b_coordbubbles1 = x_b_coordbubbles1 + speed
                x_b_coordbubbles2 = x_b_coordbubbles2 + speed
                x_b_coordbubbles3 = x_b_coordbubbles3 + speed
                x_b_coordbubbles4 = x_b_coordbubbles4 + speed
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
                
                x_coordbubbles1 = x_coordbubbles1 - speed
                x_coordbubbles2 = x_coordbubbles2 - speed
                x_coordbubbles3 = x_coordbubbles3 - speed
                x_coordbubbles4 = x_coordbubbles4 - speed
                
                x_b_coordbubbles1 = x_b_coordbubbles1 - speed
                x_b_coordbubbles2 = x_b_coordbubbles2 - speed
                x_b_coordbubbles3 = x_b_coordbubbles3 - speed
                x_b_coordbubbles4 = x_b_coordbubbles4 - speed
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
        ###AIR GAUGE###
        drawgauge(screen, x_coordgauge, y_coordgauge) #This way the air gauge is always in the background  
        ta = "Total air:" + str(total_air)
        airtext = font.render(ta, 1, black)
        screen.blit(airtext, (x_coordgauge, y_coordgauge))
        ##AirGauge##
        
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
        
        drawbubbles(screen, x_coordbubbles1, y_coordbubbles1)
        drawbubbles(screen, x_coordbubbles2, y_coordbubbles2)
        drawbubbles(screen, x_coordbubbles3, y_coordbubbles3)
        drawbubbles(screen, x_coordbubbles4, y_coordbubbles4)
     
        drawbubbles(screen, x_b_coordbubbles1, y_b_coordbubbles1)
        drawbubbles(screen, x_b_coordbubbles2, y_b_coordbubbles2)
        drawbubbles(screen, x_b_coordbubbles3, y_b_coordbubbles3)
        drawbubbles(screen, x_b_coordbubbles4, y_b_coordbubbles4)
        
        player_c = [x_coord, y_coord, 224, 188] # full box
        buddy_c = [x_coordbuddy, y_coordbuddy, 224, 188] # full box
        eel_c = [x_coordeel, y_coordeel, 200, 46]
        treasure_c = [x_coordtreasure, y_coordtreasure, 120, 100]
        cfishmedium_c = [x_coordcfishmedium, y_coordcfishmedium, 100, 45]
        
        if collision(player_c, treasure_c):
            drawtreasurebig(screen, 276, 187)
        if collision(player_c, eel_c):
            draweel(screen, 243, 322)
        if collision(player_c, cfishmedium_c):
            drawcfish(screen, 274, 278)
            
        
        drawmenu(screen, x_menu, y_menu)
            
########################################################
     
 
        
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
      
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
      
# Close the window and quit.ti
# If you forget this line, the program will 'hang'
# on exit if running from IDLE (indeed it will I found this out the hard way)
pygame.quit ()


