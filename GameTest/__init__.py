import pygame, sys
pygame.init()
<<<<<<< HEAD
    
class Diver:
=======

class Diver():
>>>>>>> f8cd8e3988583d7c061175701749b1cdfa2a9988
    diverX = 0 #Starting position
    diverY = 0
    moveX = 10
    moveY = 10 #Movement speed in the x and y direction for the diver. 
    image = None #Placeholder. Actual sprite will go here
    
def __init__(self, x, y): #Constructor would also take in the image here but since we have no image yet I'm just using a rectangle
<<<<<<< HEAD
    self.image = pygame.draw.rect(pygame.display.get_surface(), pygame.color.Color("red"),(x, y, 15, 10), 2)
    self.diverX = x
    self.diverY = y
    
def update(self):
    self.move()
    #Moves right or left according to key input
def move(self):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.diverX+= self.moveX
            elif event.type == pygame.K_LEFT:
                self.diverX-= self.moveX
            elif event.type == pygame.K_UP:
                self.diverY-=self.moveY
            elif event.type == pygame.K_DOWN:
                self.diverY+=self.moveY

def draw(self):
    pygame.display.get_surface().blit(self.image, (self.diverX, self.diverY))    

#def main():           
=======
    self.image = pygame.draw.rect(background, pygame.color.Color("red"),(x,y,15,10), 2)
    self.diverX = x
    self.diverY = y
    
def update(self):
    self.move()
    #Moves right or left according to key input
def move(self):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.diverX+= self.moveX
            elif event.type == pygame.K_LEFT:
                self.diverX-= self.moveX
            elif event.type == pygame.K_UP:
                self.diverY-=self.moveY
            elif event.type == pygame.K_DOWN:
                self.diverY+=self.moveY
def draw(self):
    screen.blit(self.image, (self.diverX, self.diverY))
    

>>>>>>> f8cd8e3988583d7c061175701749b1cdfa2a9988
screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("Hello, world!")
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((127, 255, 0))
clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)
text = font.render("Hi Comp 585", 1, (0, 0, 0))
textpos = text.get_rect()
textpos.centerx = background.get_rect().centerx
textpos.centery = background.get_rect().centery
background.blit(text, textpos)
<<<<<<< HEAD
=======
keepGoing = True
>>>>>>> f8cd8e3988583d7c061175701749b1cdfa2a9988
scubadiver = Diver(10, 10)

while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
<<<<<<< HEAD
            sys.exit()

=======
            keepGoing = False   
        
>>>>>>> f8cd8e3988583d7c061175701749b1cdfa2a9988
    screen.blit(background, (0,0))
    scubadiver.update()
    scubadiver.draw()
    pygame.display.update()