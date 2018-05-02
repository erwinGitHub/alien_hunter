import pygame
from pygame.sprite import Sprite
from pygame.font import Font

class Label(Sprite):
    """Class to manage labels"""
    
    def __init__(self, screen, text='', x=0, y=0):
        """Initiation of object label"""
        super().__init__()
        
        #Some defaults
        self.text = text
        self.text_color = (180, 180, 180)
        self.text_size = 36
        self.screen = screen
        self.x = x
        self.y = y
        self.font = Font(None, self.text_size)
        self.text_img = self.font.render(self.text, True, self.text_color)
        self.text_rect = self.text_img.get_rect()
        self.text_rect.left = self.x
        self.text_rect.top = self.y
        
        
    def update(self):
        """draw label on the screen"""
        self.text_img = self.font.render(self.text, True, self.text_color)
        self.screen.blit(self.text_img, self.text_rect)
