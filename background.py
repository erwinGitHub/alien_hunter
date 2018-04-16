import pygame

class Background():
    """Class which describes background"""

    def __init__(self, game_settings, screen):
        """Background initiation and its initial position"""
        self.screen = screen
        
        self.image = pygame.image.load(game_settings.background_image)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #Set background initial position
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        
        
    def update(self):
        pass
        

    def draw(self):
        """Load background image on the screen"""
        self.screen.blit(self.image, self.rect)
        

