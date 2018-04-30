import pygame
from game_object import GameObject
from pygame.font import Font

class Button(GameObject):
    """Class to manage buttons"""
    
    def __init__(self, game_objects,  text='', x=0, y=0, width=2, height=2):
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

        self.screen = game_objects["screen"].screen
        self.rect = pygame.Rect(x, y, width, height)
        
        #Set text on button
        if self.text != '':
            f = Font(None, self.text_size)
            self.text_img = f.render(self.text, True, self.text_color)
            self.text_rect = self.text_img.get_rect()
            self.rect.width = self.text_rect.width + self.text_size
            self.rect.height = self.text_rect.height + self.text_size
            self.text_rect.center = self.rect.center
        
        
    def update_me(self, mouse_pos, clicked=False):
        """Update current color of buton depend on mouse position"""
        if self.rect.collidepoint(mouse_pos):
            if clicked:
                self.current_color = self.click_color
            else:
                self.current_color = self.highlight_color
        else:
            self.current_color = self.color

    def draw(self):
        """draw button on the screen"""
        pygame.draw.rect(self.screen, self.border_color, self.rect)
        b = pygame.Rect(self.rect.x+1, self.rect.y+1, self.rect.width-2, self.rect.height-2)
        pygame.draw.rect(self.screen, self.current_color, b)
        
        if self.text != '':
            self.screen.blit(self.text_img, self.text_rect)