import pygame
from game_manager import screen_settings
from pygame.locals import *

class Player(pygame.sprite.Sprite):
  def __init__(self, player):
    super(Player, self).__init__()
    self.surf = pygame.Surface((7.5, 85))       #player deminsions
    self.surf.fill((255, 255, 255))             #player color
    self.score = 0
    self.player = player

    if self.player == 1:    # Detemines if player 1 or player 2  
      self.rect = self.surf.get_rect(center=(10,((screen_settings['height'] - self.surf.get_height()) /2)))
    elif self.player == 2:
      self.rect = self.surf.get_rect(center=((screen_settings['width'] - 10) ,((screen_settings['height'] - self.surf.get_height()) /2)))

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
    if self.rect.bottom >= screen_settings['height']:
      self.rect.bottom = screen_settings['height']