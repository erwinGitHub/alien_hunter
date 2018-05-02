import pygame
from pygame.sprite import Sprite
from pygame.font import Font

class Button(Sprite):
    """Class to manage buttons"""
    
    def __init__(self, screen, text=None, x=0, y=0, width=100, height=50, action=None):
        """Initiation of object button"""
        super().__init__()
        
        #Some defaults
        self.color = (170, 170, 170)
        self.highlight_color = (200, 200, 200)
        self.click_color = (130, 130, 130)
        self.current_color = self.color
        self.border_color = (0, 193, 193)
        self.text = text
        self.text_color = (0, 0, 0)
        self.text_size = 36

        self.screen = screen
        self.rect = pygame.Rect(x, y, width, height)
        self.action = action
        
        #Set text on button
        if self.text != None:
            f = Font(None, self.text_size)
            self.text_img = f.render(self.text, True, self.text_color)
            self.text_rect = self.text_img.get_rect()
            self.rect.width = self.text_rect.width + self.text_size
            self.rect.height = self.text_rect.height + self.text_size
        
        
    def update_me(self, mouse_pos, clicked=False):
        """Update current color of buton depend on mouse position"""
        if self.rect.collidepoint(mouse_pos):
            if clicked:
                self.current_color = self.click_color
            else:
                self.current_color = self.highlight_color
        else:
            self.current_color = self.color

    def update(self):
        """draw button on the screen"""
        self.text_rect.center = self.rect.center
        pygame.draw.rect(self.screen, self.border_color, self.rect)
        b = pygame.Rect(self.rect.x+1, self.rect.y+1, self.rect.width-2, self.rect.height-2)
        pygame.draw.rect(self.screen, self.current_color, b)
        
        if self.text != None:
            self.screen.blit(self.text_img, self.text_rect)
