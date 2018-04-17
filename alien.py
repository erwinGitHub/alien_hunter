import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class which describes one alien ship"""
    
    def __init__(self, game_settings, screen, x, y):
        """init object settings"""
        super(Alien, self).__init__()
        self.screen = screen
        self.game_settings = game_settings
        
        #load alien image
        self.image = pygame.image.load(game_settings.alien_image)
        self.rect = self.image.get_rect()
        
        #Set initial position for alien ship
        self.rect.x = x
        self.rect.y = y
        
        #Save precission position of alien ship
        self.x = float(self.rect.x)
        
    def update(self):
        pass      
