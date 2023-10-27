import pygame, sys
import math
import random

pygame.init()

#setting the screen up, logo, font, music
Main_surf = pygame.display.set_mode((1400,750))
pygame.display.set_caption('Star wars ripoff')
logo = pygame.image.load('Images\\logo.png')
pygame.display.set_icon(logo)
font_20=pygame.font.Font('pixel.ttf',20)
font_40=pygame.font.Font('pixel.ttf',40)
font_60=pygame.font.Font('pixel.ttf',60)
bg_music = pygame.mixer.Sound('audio\\music.mp3')
bg_music.play(loops = -1)
clock = pygame.time.Clock()
game_event=0

#intro screen setup
intro_scrn=pygame.image.load('Images\\Space Background 1.png').convert_alpha()
intro_x1=1400
intro_x2=0
intro_msg_1=font_20.render('Dog in a Box Studio presents:', False, 'Green')
intro_msg_rect1=intro_msg_1.get_rect(center=(700,50))
intro_msg_2=font_60.render('Star wars ripoff', False, 'Blue')
intro_msg_rect2=intro_msg_2.get_rect(center=(700,150))
Start_button=font_40.render('press space to begin', False, (100,0,100))
Start_button_rect=Start_button.get_rect(center=(700,400))
spaceship_show=pygame.image.load('Images\\sma.png').convert_alpha()


#playing screen1 setup
scrn1=pygame.image.load('Images\\Space Background 2.png').convert_alpha()
intro_y1=750
intro_y2=0
def score_disp():
    score=int(pygame.time.get_ticks()/1000)
    Score_msg=font_20.render(f'Timer:{score}', False, 'Green')
    Score_msg_rect=Score_msg.get_rect(bottomleft=(100,50))
    Main_surf.blit(Score_msg,Score_msg_rect)




#player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()



#enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()

        if game_event==0:
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                    game_event=1
        else:
            a=1
            
     
    if game_event==0:
        #background animations
        Main_surf.blit(intro_scrn,(intro_x1,0))
        Main_surf.blit(intro_scrn,(intro_x2,0))
        intro_x1-=1
        intro_x2-=1
        if intro_x1<0: intro_x1=1400
        if intro_x2<-1400: intro_x2=0
        Main_surf.blit(intro_msg_1,intro_msg_rect1)
        Main_surf.blit(intro_msg_2,intro_msg_rect2)
        pygame.draw.rect(Main_surf,(100,0,100),Start_button_rect,2)
        Main_surf.blit(Start_button,Start_button_rect)


        #spaceship move weird animation
        '''x_sine = intro_x1 / 5  % 1400
        y_sine = int(math.sin(x_sine/50.0) * 50 + 400)   
        Main_surf.blit(spaceship_show,(x_sine,y_sine+100))
        Main_surf.blit(spaceship_show,(x_sine+200,y_sine))
        Main_surf.blit(spaceship_show,(x_sine-200,y_sine))'''

        

    elif game_event==1:
        #background animation for level1
        Main_surf.blit(scrn1,(0,intro_y1))
        Main_surf.blit(scrn1,(0,intro_y2))
        intro_y1-=1
        intro_y2-=1
        if intro_y1<0: intro_y1=750
        if intro_y2<-750: intro_y2=0

        score_disp()



    pygame.display.update()
    clock.tick(60)
