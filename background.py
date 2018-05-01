import pygame
from game_object import GameObject

class Background(GameObject):
    """Class which describes background"""

    def __init__(self, screen, game_settings):
        """Background initiation and its initial position"""
        
        super().__init__()
                
        self.image = pygame.image.load(game_settings.background_image)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #Set background initial position
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

