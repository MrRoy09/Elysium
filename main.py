import pygame, sys, math
from random import randint
import numpy as np

class EnemyPlayer(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image=pygame.image.load('Images\\ship2.png')
        self.rect=self.image.get_rect(center=pos)

    def player_input(self):
        Keys = pygame.key.get_pressed()
        if Keys[pygame.K_d]:
            self.rect.x += 10
        elif Keys[pygame.K_a]:
            self.rect.x -= 10

    def player_movement(self):
        if self.rect.left<=0:self.rect.left=0
        if self.rect.right>=1400:self.rect.right=1400       

    def update(self):
        self.player_input()
        self.player_movement()

class Player (pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image=pygame.image.load('Images\\ship1.png')
        self.rect=self.image.get_rect(center=pos)
    
    def player_input(self):
        Keys = pygame.key.get_pressed()
        if Keys[pygame.K_RIGHT]:
            self.rect.x += 10
        elif Keys[pygame.K_LEFT]:
            self.rect.x -= 10
    
    def mov_const(self):
        if self.rect.right<=1400: self.rect.right=1400
        if self.rect.left>=0: self.rect.right=0

    def update(self):
        self.player_input()
        self.mov_const()

class asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load('Images\\asteroid1.png')
        self.rect = self.image.get_rect(midbottom = (randint(200,1400),0))

    def update(self,spx,spy):
        self.rect.x -= spx
        self.rect.y += spy
        self.destroy()
    
    def destroy(self):
        if self.rect.x <= -100: 
             self.kill()    
        if self.rect.y >= 900:
             self.kill()

class Game:
    intro_y1=-750
    intro_y2=0
    start_time=0
    
    def __init__(self):
        player1_ship=Player((700,300))
        self.player1=pygame.sprite.GroupSingle(player1_ship)
        player2_ship=EnemyPlayer((700,700))
        self.player2=pygame.sprite.GroupSingle(player2_ship)

    def background(self):
        Main_surf.blit(scrn1,(0,intro_y1))
        Main_surf.blit(scrn1,(0,intro_y2))
        intro_y1+=2
        intro_y2+=2
        if intro_y1>750: intro_y1=-750
        if intro_y2>750: intro_y2=-750

    '''def score_disp(self):
        score=int(pygame.time.get_ticks()/1000)-start_time
        Score_msg=font_20.render(f'Timer:{score}', False, 'Green')
        Score_msg_rect=Score_msg.get_rect(bottomleft=(100,50))
        Main_surf.blit(Score_msg,Score_msg_rect)
'''
    def run(self):
        self.background()
        self.player1.update()
        self.player1.draw(Main_surf)
        self.player2.update()
        self.player2.draw(Main_surf)


    
if __name__=='__main__':
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
    a=0
    game=Game()


    #intro screen setup
    intro_scrn=pygame.image.load('Images\\Space Background 1.png').convert_alpha()
    intro_x1=1400
    intro_x2=0
    intro_msg_1=font_20.render('Dog in a Box Studio presents:', False, 'Green')
    intro_msg_rect1=intro_msg_1.get_rect(center=(700,50))
    intro_msg_2=font_60.render('Star wars ripoff', False, 'Blue')
    intro_msg_rect2=intro_msg_2.get_rect(center=(700,150))
    Start_button=font_40.render('press space to begin', False, (255,0,100))
    Start_button_rect=Start_button.get_rect(center=(700,400))
    spaceship_show=pygame.image.load('Images\\sma.png').convert_alpha()
    connect1=pygame.image.load('Images\\disconnect.png').convert_alpha()
    connect1_rect=connect1.get_rect(center=(300,600))
    connect1_text=font_20.render('Connection 1', False, 'Green')
    connect1_text_rect=connect1_text.get_rect(center=(300,700))
    if a==1: connect1=pygame.image.load('Images\\connected.png').convert_alpha()
    connect2=pygame.image.load('Images\\disconnect.png').convert_alpha()
    connect2_rect=connect2.get_rect(center=(1100,600))
    connect2_text=font_20.render('Connection 2', False, 'Green')
    connect2_text_rect=connect1_text.get_rect(center=(1100,700))
    if a==1: connect1=pygame.image.load('Images\\connected.png').convert_alpha()


    asteroid1=pygame.sprite.Group()
    astrid_timer=pygame.USEREVENT + 1
    pygame.time.set_timer(astrid_timer,randint(1000,2500))

    #playing screen1 setup
    scrn1=pygame.image.load('Images\\Space Background 2.png').convert_alpha()
    intro_y1=-750
    intro_y2=0
    def score_disp():
        score=int(pygame.time.get_ticks()/1000)-start_time
        Score_msg=font_20.render(f'Timer:{score}', False, 'Green')
        Score_msg_rect=Score_msg.get_rect(bottomleft=(100,50))
        Main_surf.blit(Score_msg,Score_msg_rect)


    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()

            if game_event==0:
                if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                        game_event=1
                        start_time=int(pygame.time.get_ticks()/1000) 
                if event.type==astrid_timer:
                    asteroid1.add(asteroid())
            
            elif game_event==1:
                if event.type==astrid_timer:
                    asteroid1.add(asteroid())

            else: a=1
                
        
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
            pygame.draw.rect(Main_surf,(255,0,100),Start_button_rect,2)
            Main_surf.blit(Start_button,Start_button_rect)
            Main_surf.blit(connect1,connect1_rect)
            Main_surf.blit(connect2,connect2_rect)
            Main_surf.blit(connect1_text,connect1_text_rect)
            Main_surf.blit(connect2_text,connect2_text_rect)

            
            asteroid1.draw(Main_surf)
            asteroid1.update(2,2)

            #spaceship move weird animation
            x_sine = pygame.time.get_ticks() / 5  % 1400
            y_sine = int(math.sin(x_sine/50.0) * 50 + 400)  
            Main_surf.blit(spaceship_show,(x_sine,y_sine))


        elif game_event==1:
            #background animation for level1
            '''Main_surf.blit(scrn1,(0,intro_y1))
            Main_surf.blit(scrn1,(0,intro_y2))
            intro_y1+=2
            intro_y2+=2
            if intro_y1>750: intro_y1=-750
            if intro_y2>750: intro_y2=-750

            game.run() 
            asteroid1.draw(Main_surf)
            asteroid1.update(0,3)

            score_disp()'''
            game.run()

        pygame.display.update()
        clock.tick(60)