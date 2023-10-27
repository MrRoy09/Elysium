import pygame, sys
pygame.init()

#setting the screen up, logo, font, music
Main_surf = pygame.display.set_mode((1400,750))
pygame.display.set_caption('Star wars ripoff')
logo = pygame.image.load('Images\\logo.png')
pygame.display.set_icon(logo)
font=pygame.font.Font('pixel.ttf')
bg_music = pygame.mixer.Sound('audio\\music.mp3')
bg_music.play(loops = -1)
clock = pygame.time.Clock()
game_active=False

#background setup
backg=pygame.image.load('Images\\Space Background.png').convert_alpha()
x1=1400
x2=0
intro_msg=font.render('Welcome to the start of the game', False, 'Green')
intro_msg_rect=intro_msg.get_rect(center=(700,50))

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
     
    
    if game_active:
        a=1
    else:
        #background animations
        Main_surf.blit(backg,(x1,0))
        Main_surf.blit(backg,(x2,0))
        x1-=1
        x2-=1
        if x1<0: x1=1400
        if x2<-1400: x2=0
        Main_surf.blit(intro_msg,intro_msg_rect)
        Main_surf.blit()
        

    pygame.display.update()
    clock.tick(60)
