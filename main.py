import pygame, sys, math
from random import randint

pygame.init()

class EnemyPlayer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load('Images\\ship2.png')
        self.rect=self.image.get_rect(center=(700,700))

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
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load('Images\\ship1.png')
        self.rect=self.image.get_rect(center=(700,400))
    
    def player_input(self):
        Keys = pygame.key.get_pressed()
        if Keys[pygame.K_RIGHT]:
            self.rect.x += 10
        elif Keys[pygame.K_LEFT]:
            self.rect.x -= 10
    
    def player_movement(self):
        self.rect.y-=0.1
        if self.rect.left<=0:self.rect.left=0
        if self.rect.right>=1400:self.rect.right=1400


    def update(self):
        self.player_input()
        self.player_movement()

class asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load('Images\\asteroid1.png')
        self.rect=self.image.get_rect(topleft=(700,200))
    
    def asteroid_movement(self,x,y):
        self.rect.x += x
        self.rect.y += y
        if self.rect.left==1450: 
            self.rect.right=0
        if self.rect.right==-50:
            self.rect.left=1400
        if self.rect.top==750:
            self.rect.bottom=50
        if self.rect.bottom==0:
            self.rect.top=730
        

    def update(self,x,y):
        self.asteroid_movement(x,y)


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
Start_button=font_40.render('press space to begin', False, (255,0,100))
Start_button_rect=Start_button.get_rect(center=(700,400))
spaceship_show=pygame.image.load('Images\\sma.png').convert_alpha()

#playing screen1 setup
scrn1=pygame.image.load('Images\\Space Background 2.png').convert_alpha()
intro_y1=-750
intro_y2=0
def score_disp():
    score=int(pygame.time.get_ticks()/1000)-start_time
    Score_msg=font_20.render(f'Timer:{score}', False, 'Green')
    Score_msg_rect=Score_msg.get_rect(bottomleft=(100,50))
    Main_surf.blit(Score_msg,Score_msg_rect)
player1_ship=pygame.sprite.GroupSingle()
player1_ship.add(Player())
player2_ship=pygame.sprite.GroupSingle()
player2_ship.add(EnemyPlayer())
asteroid1=pygame.sprite.Group()
asteroid1.add(asteroid())
asteroid2=pygame.sprite.Group()
asteroid2.add(asteroid())



start_time=0


x1=randint(-5,5)
y1=randint(-5,5)
x2=randint(-5,5)
y2=randint(-5,5)


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()

        if game_event==0:
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                    game_event=1
                    start_time=int(pygame.time.get_ticks()/1000) 
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
        
        
        asteroid1.draw(Main_surf)
        asteroid1.update(x1,y1)
        asteroid2.draw(Main_surf)
        asteroid2.update(x2,y2)

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

        player1_ship.draw(Main_surf)
        player1_ship.update()
        player2_ship.draw(Main_surf)
        player2_ship.update()
        asteroid1.draw(Main_surf)
        asteroid1.update(x1,y1)
        asteroid2.draw(Main_surf)
        asteroid2.update(x2,y2)
        score_disp()




    pygame.display.update()
    clock.tick(60)
