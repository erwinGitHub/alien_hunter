import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class to manage bullets"""
    
    def __init__(self, screen, game_settings, centerx, top):
        """Initiation of object bullet"""
        super().__init__()
        
        self.screen = screen
        self.game_settings = game_settings
        self.rect = pygame.Rect(0, 0, self.game_settings.bullet_width,
            self.game_settings.bullet_height)
        self.rect.centerx = centerx
        self.rect.top = top
        
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        
        self.color = self.game_settings.bullet_color
        self.speed_factor = self.game_settings.bullet_speed_factor

    def update(self):
        """
        definition of bullet movement
        Only this method will be used from Group o sprites
        """
        self.y -= self.speed_factor
        self.rect.y = self.y
        self.draw()
        
    def draw(self):
        """draw bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
