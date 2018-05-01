import pygame
from pygame.sprite import Sprite

class Background(Sprite):
    """Class which describes background"""

    def __init__(self, screen, game_settings):
        """Background initiation and its initial position"""
        super().__init__()
        self.image = pygame.image.load(game_settings.background_image)
        self.rect = self.image.get_rect()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        
        #Set background initial position
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.draw()
