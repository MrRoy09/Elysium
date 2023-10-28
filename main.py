import pygame, sys, math
from random import randint
import numpy as np

class Player (pygame.sprite.Sprite):
     def __init__(self,pos):
        super().__init__()
        self.image=pygame.image.load('Images\\ship1.png')
        self.rect=self.image.get_rect(center=pos)
        self.ready = True
        self.laser_time = 0
        self.laser_cooldown = 600

        self.lasers = pygame.sprite.Group()
        self.laser_sound = pygame.mixer.Sound('audio\\laser.mp3')
        self.laser_sound.set_volume(0.5)
    
     def player_input(self):
        Keys = pygame.key.get_pressed()
        if Keys[pygame.K_RIGHT]:
            self.rect.x += 10
        elif Keys[pygame.K_LEFT]:
            self.rect.x -= 10

        if Keys[pygame.K_UP]:
            self.laser_shoot()
            self.ready = False
            self.laser_time = pygame.time.get_ticks()
            self.laser_sound.play()
    
     def recharge(self):
        if not self.ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time >= self.laser_cooldown:
                 self.ready = True
    
     def laser_shoot(self):
        self.lasers.add(Laser(self.rect.center,-8))

     def mov_const(self):
        if self.rect.right<=1400: self.rect.right=1400
        if self.rect.left>=0: self.rect.right=0

     def update(self):
        self.player_input()
        self.mov_const()
        self.recharge()
        self.lasers.update()
    
class EnemyPlayer(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image=pygame.image.load('Images\\ship2.png')
        self.rect=self.image.get_rect(center=pos)
        self.ready = True
        self.laser_time = 0
        self.laser_cooldown = 600

        self.lasers = pygame.sprite.Group()
        self.laser_sound = pygame.mixer.Sound('audio\\laser.mp3')
        self.laser_sound.set_volume(0.5)
    
    def player_input(self):
        Keys = pygame.key.get_pressed()
        if Keys[pygame.K_d]:
            self.rect.x += 10
        elif Keys[pygame.K_a]:
            self.rect.x -= 10
        if Keys[pygame.K_q]:
            self.laser_shoot()
            self.ready = False
            self.laser_time = pygame.time.get_ticks()
            self.laser_sound.play()
    
    def recharge(self):
        if not self.ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time >= self.laser_cooldown:
                 self.ready = True
    
    def laser_shoot(self):
        self.lasers.add(Laser(self.rect.center,-8))

    def mov_const(self):
        if self.rect.right<=1400: self.rect.right=1400
        if self.rect.left>=0: self.rect.right=0

    def update(self):
        self.player_input()
        self.mov_const()
        self.recharge()
        self.lasers.update()

class Laser(pygame.sprite.Sprite):
	def __init__(self,pos,speed):
		super().__init__()
		self.image = pygame.Surface((4,20))
		self.image.fill('white')
		self.rect = self.image.get_rect(center = pos)
		self.speed = speed
		self.height_y_constraint = 750

	def destroy(self):
		if self.rect.y <= -50 or self.rect.y >= self.height_y_constraint + 50:
			self.kill()

	def update(self):
		self.rect.y += self.speed
		self.destroy()

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
    def __init__(self):
        player1_ship=Player((700,300))
        self.playermp=pygame.sprite.GroupSingle(player1_ship)
        player2_ship=EnemyPlayer((700,700))
        self.playerep=pygame.sprite.GroupSingle(player2_ship)

    def run_ep(self):
        self.playermp.update()
        self.playermp.draw(Main_surf)
        self.playerep.update()
        self.playerep.draw(Main_surf)
    
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
    b=1
    game=Game()

    if a==0:
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
        if b==1: 
            connect1=pygame.image.load('Images\\connected.png').convert_alpha()
        connect2=pygame.image.load('Images\\disconnect.png').convert_alpha()
        connect2_rect=connect2.get_rect(center=(1100,600))
        connect2_text=font_20.render('Connection 2', False, 'Green')
        connect2_text_rect=connect1_text.get_rect(center=(1100,700))
        if b==1: 
            connect2=pygame.image.load('Images\\connected.png').convert_alpha()


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
            Main_surf.blit(scrn1,(0,intro_y1))
            Main_surf.blit(scrn1,(0,intro_y2))
            intro_y1+=2
            intro_y2+=2
            if intro_y1>750: intro_y1=-750
            if intro_y2>750: intro_y2=-750

            def score_disp():
                score=int(pygame.time.get_ticks()/1000)-start_time
                Score_msg=font_20.render(f'Timer:{score}', False, 'Green')
                Score_msg_rect=Score_msg.get_rect(bottomleft=(100,50))
                Main_surf.blit(Score_msg,Score_msg_rect)
            score_disp()  

            game.run_ep()


        pygame.display.update()
        clock.tick(60)