#! usr/bin/python3
# Pong game in python 
# First game in python without following tutorial 
 
import pygame, random
from os.path import join
from pygame.locals import *


# Initialize pygame library
pygame.mixer.init(frequency=22050, size=-16, channels=1, buffer=64)
pygame.init()
try:
    blip = pygame.mixer.Sound(join("assests","sounds","blip.wav"))
except
    blip = pygame.mixer.Sound(join("assests","sounds","blip.ogg"))
    
    


clock = pygame.time.Clock()

# Sets Visual and text
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')
pygame.display.set_icon(pygame.image.load(join('visuals','gaming.png')))
font = pygame.font.Font(join('visuals','bit5x3.ttf'), 100)



class Player(pygame.sprite.Sprite):
    def __init__(self, player):
        super(Player, self).__init__()
        self.surf = pygame.Surface((7.5, 85))       #player deminsions
        self.surf.fill((255, 255, 255))             #player color
        self.score = 0
        self.player = player
        if self.player == 1:    # Detemines if player 1 or player 2  
            self.rect = self.surf.get_rect(center=(10,((screen_height - self.surf.get_height()) /2)))
        elif self.player == 2:
            self.rect = self.surf.get_rect(center=((screen_width - 10) ,((screen_height - self.surf.get_height()) /2)))

    def update(self, pressed_keys):
        """ Moves the player """
        if self.player == 1:
            if pressed_keys[K_w]:
                self.rect.move_ip(0, -8)
            if pressed_keys[K_s]:
                self.rect.move_ip(0, 8)
        elif self.player == 2:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -8)
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 8)
        
       # Keep player on the screen
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super(Ball, self).__init__()
        self.speed_x = 7 * random.choice((1,-1))
        self.speed_y = 7 * random.choice((1,-1))
        self.surf = pygame.Surface((20,20))
        self.color = (255, 255, 255)
        self.rect = self.surf.get_rect(center=(((screen_width - self.surf.get_width()) / 2),((screen_height - self.surf.get_height()) / 2)))


    def update(self,player_1, player_2):
        """ Moves the ball around
            And gives the score """
        
        self.rect.move_ip(self.speed_x,self.speed_y)

        # keeps the ball on screen and bounces the ball around 
        if self.rect.top <= 0 or self.rect.bottom >= screen_height:
            blip.play()
            self.speed_y *= -1
        
        # Resets the ball and gives score  
        if self.rect.left <= 0:
            self.rect.center = (screen_width / 2 , screen_height / 2)
            self.speed_y *= random.choice((1,-1))
            self.speed_x *= random.choice((1,-1))
            player_1.score += 1      
        elif self.rect.right >= screen_width:
            self.rect.center = (screen_width / 2 , screen_height / 2)
            self.speed_y *= random.choice((1,-1))
            self.speed_x *= random.choice((1,-1))
            player_2.score += 1
           
            

player_1 = Player(1)
player_2 = Player(2)
ball = Ball()


running = True 

while running:
    # Allow the user to leave the game/ end game loop 
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False     
        elif event.type == QUIT:
            running = False 
    
    #  Ball collision with player
    if ball.rect.colliderect(player_1) or ball.rect.colliderect(player_2):
        blip.play()
        ball.speed_x *= -1

    
    # player movements 
    pressed_keys = pygame.key.get_pressed()
    player_1.update(pressed_keys)
    player_2.update(pressed_keys)

    # Ball movements
    ball.update(player_1=player_1,player_2=player_2)
    
    # give screen it back ground color
    screen.fill((40, 40, 40))


    # Draws the players
    screen.blit(player_1.surf, player_1.rect)
    screen.blit(player_2.surf, player_2.rect)

    # Draws the line and ball
    pygame.draw.ellipse(screen, ball.color, ball.rect)
    pygame.draw.aaline(screen, (255, 255, 255), (screen_width / 2, 0),(screen_width / 2, screen_height))

    # Draws the the score 
    screen.blit(font.render(str(player_1.score),False,(255, 255, 255)),(int(screen_width / 1.3329), 10))
    screen.blit(font.render(str(player_2.score),False,(255, 255, 255)),(screen_width / 4, 10))

    pygame.display.flip()


    clock.tick(60)


pygame.quit()