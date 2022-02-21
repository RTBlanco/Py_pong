import pygame, random
from os.path import join
from pygame.locals import *


# Initialize pygame library
pygame.mixer.init(frequency=22050, size=-16, channels=1, buffer=64)
pygame.init()

# Issue that mac and window handle the sound differently 
try:
    blip = pygame.mixer.Sound(join("assests","sounds","blip.wav"))
except:
    blip = pygame.mixer.Sound(join("assests","sounds","blip.ogg"))
    
    


clock = pygame.time.Clock()

# Sets Visual and text
screen_settings = {
  'height' : 400,
  'width' : 800
}

screen = pygame.display.set_mode((screen_settings['width'], screen_settings['height']))
pygame.display.set_caption('Pong')
pygame.display.set_icon(pygame.image.load(join('assests','visuals','gaming.png')))
font = pygame.font.Font(join('assests','visuals','bit5x3.ttf'), 100)
