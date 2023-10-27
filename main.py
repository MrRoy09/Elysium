import pygame, sys

pygame.init()

Main_surf = pygame.display.set_mode((1400,750))
pygame.display.set_caption('Star wars ripoff')
clock = pygame.time.Clock()
game_active=True

#background setup
backg=pygame.image.load('Space Background.png').convert_alpha()
x1=1400
x2=0
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    
    if game_active:
        #background animantions
        Main_surf.blit(backg,(x1,0))
        Main_surf.blit(backg,(x2,0))
        x1-=1
        x2-=1
        if x1<0: x1=1400
        if x2<-1400: x2=0    
    
    pygame.display.update()
    clock.tick(60)
