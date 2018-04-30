import pygame
from game_object import GameObject

class Bullet(GameObject):
    """Class to manage bullets"""
    
    def __init__(self, game_objects):
        """Initiation of object bullet"""
        super().__init__()
        
        self.screen = game_objects["screen"].screen
        self.game_settings = game_objects["game_settings"]
        self.ship = game_objects["ship"]
        self.rect = pygame.Rect(0, 0, self.game_settings.bullet_width,
            self.game_settings.bullet_height)
        self.rect.centerx = self.ship.rect.centerx
        self.rect.top = self.ship.rect.top
        
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
        
    def draw_me(self):
        """draw bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
