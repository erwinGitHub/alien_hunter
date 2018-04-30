import pygame
from game_object import GameObject

class Screen(GameObject):
    """Class which describes background"""

    def __init__(self, game_objects):
        """Background initiation and its initial position"""
        
        super().__init__()
        
        self.game_settings = game_objects["game_settings"]        
        self.screen = pygame.display.set_mode(
            (self.game_settings.screen_width, self.game_settings.screen_height))
