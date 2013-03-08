import pygame
from PIL import Image
pygame.init()
# Dennis Branch

#######################################################
pg = pygame
clock = pg.time.Clock()
#######################################################


background1 = pg.image.load("TreasureMap.jpg")
screen1 = pg.display.set_mode((1024, 768))
#######################################################

background2 = pg.image.load("Aquarium.jpg")

screen2 = pg.display.set_mode((1024, 768))

#######################################################

screenswitch = 0
keepGoing = True
while keepGoing:
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            keepGoing = False
            
    if screenswitch == 0:
        screen1.blit(background1, (0,0))
        pg.display.flip()  
        #screenswitch = 1
    else:
        screen2.blit(background2, (0,0))
        pg.display.flip()
        #screenswitch = 0
        
    
    if event.type == pygame.MOUSEBUTTONUP:
            #screen1.blit(background1, (0,0))
            #pg.display.flip()  
        screenswitch = 1       
    else:
            #screen2.blit(background2, (0,0))
            #pg.display.flip()
        screenswitch = 0
    