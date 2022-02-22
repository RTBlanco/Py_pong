import pygame, random
from game_manager import blip, screen_settings

class Ball(pygame.sprite.Sprite):
  def __init__(self):
    super(Ball, self).__init__()
    self.speed_x = 7 * random.choice((1,-1))
    self.speed_y = 7 * random.choice((1,-1))
    self.surf = pygame.Surface((20,20))
    self.color = (255, 255, 255)
    self.rect = self.surf.get_rect(center=(((screen_settings['width'] - self.surf.get_width()) / 2),((screen_settings['height'] - self.surf.get_height()) / 2)))


  def update(self,player_1, player_2):
    """ Moves the ball around
        And gives the score """
    
    self.rect.move_ip(self.speed_x,self.speed_y)

    # keeps the ball on screen and bounces the ball around 
    if self.rect.top <= 0 or self.rect.bottom >= screen_settings['height']:
      blip.play()
      self.speed_y *= -1
    
    # Resets the ball and gives score  
    if self.rect.left <= 0:
      self.rect.center = (screen_settings['width'] / 2 , screen_settings['height'] / 2)
      self.speed_y *= random.choice((1,-1))
      self.speed_x *= random.choice((1,-1))
      player_1.score += 1      
    elif self.rect.right >= screen_settings['width']:
      self.rect.center = (screen_settings['width'] / 2 , screen_settings['height'] / 2)
      self.speed_y *= random.choice((1,-1))
      self.speed_x *= random.choice((1,-1))
      player_2.score += 1