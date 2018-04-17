import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class to manage bullets"""
    
    def __init__(self, game_settings, screen, ship):
        """Initiation of object bullet"""
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, game_settings.bullet_width,
            game_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        
        self.color = game_settings.bullet_color
        self.speed_factor = game_settings.bullet_speed_factor

    def update(self):
        """
        definition of bullet movement
        Only this method will be used from Group o sprites
        """
        self.y -= self.speed_factor
        self.rect.y = self.y
        
    def draw_me(self):
        """draw bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
