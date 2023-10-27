import pygame, sys
pygame.init()

#setting the screen up
Main_surf = pygame.display.set_mode((1400,750))
pygame.display.set_caption('Star wars ripoff')
logo = pygame.image.load('logo,png')
pygame.display.set_icon(logo)
font=pygame.font.Font('pixel.ttf')
clock = pygame.time.Clock()
game_active=True

#background setup
backg=pygame.image.load('Space Background.png').convert_alpha()
x1=1400
x2=0

#player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()





#enemy class



while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    
    #background animantions
    Main_surf.blit(backg,(x1,0))
    Main_surf.blit(backg,(x2,0))
    x1-=1
    x2-=1
    if x1<0: x1=1400
    if x2<-1400: x2=0 
    
    if game_active:a=1
    else:
        intro_msg=font.render

    pygame.display.update()
    clock.tick(60)
