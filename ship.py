import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """Class which describes ship"""

    def __init__(self, game_settings, screen):
        """Ship initiation and its initial position"""
        self.screen = screen
        self.game_settings = game_settings
        
        self.image = pygame.image.load(game_settings.ship_image)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #Set ship initial position
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        
        #Variables which tells if ship is moveing
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
    def update(self):
        """Update ship position"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.game_settings.ship_speed_factor    
        
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.game_settings.ship_speed_factor    
        
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.game_settings.ship_speed_factor
        
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.game_settings.ship_speed_factor

        #update rectanlge position
        self.rect.centerx = self.centerx    
        self.rect.centery = self.centery    

    def draw_me(self):
        self.screen.blit(self.image, self.rect)
        
