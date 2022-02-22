import pygame
from ball.Ball import Ball
from player.Player import Player
from game_manager import screen_settings, screen, blip, font, clock
from pygame.locals import *

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
  pygame.draw.aaline(screen, (255, 255, 255), (screen_settings['width'] / 2, 0),(screen_settings['width'] / 2, screen_settings['height']))

  # Draws the the score 
  screen.blit(font.render(str(player_1.score),False,(255, 255, 255)),(int(screen_settings['width'] / 1.3329), 10))
  screen.blit(font.render(str(player_2.score),False,(255, 255, 255)),(screen_settings['width'] / 4, 10))

  pygame.display.flip()


  clock.tick(60)


pygame.quit()