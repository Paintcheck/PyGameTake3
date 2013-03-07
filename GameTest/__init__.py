import pygame
pygame.init()

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
keepGoing = True
while keepGoing:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False
                
    screen.blit(background, (0,0))
    pygame.display.flip()