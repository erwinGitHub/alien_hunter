import pygame
from pygame.sprite import Sprite
from bullet import Bullet

class Ship(Sprite):
    """Class which describes ship"""

    def __init__(self, screen, game_settings):
        """Ship initiation and its initial position"""
        
        super().__init__()
        
        self.game_settings = game_settings
        self.screen = screen
        self.images = []
        for image in self.game_settings.ship_images:
            self.images.append(pygame.image.load(image))
            
        self.rect = self.images[0].get_rect()
        self.screen_rect = self.screen.get_rect()
        self.current_image = 0
        self.shot_down = False
        
        #Set ship initial position
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        
        #Variables which tells if ship is moveing
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def draw(self):
        if self.shot_down:
            self.current_image += 1
        
        if self.current_image >= len(self.images):
            self.kill()
        else:
            self.screen.blit(self.images[self.current_image], self.rect)
        
    def update(self):
        """Update ship position"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.game_settings.ship_speed_factor    
        
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.game_settings.ship_speed_factor    
    
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.game_settings.ship_speed_factor
        
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.game_settings.ship_speed_factor

        #update rectanlge position
        self.rect.centerx = self.centerx    
        self.rect.centery = self.centery    
        
        #draw ship
        self.draw()
        
    def fire(self):
        if self.game_settings.ammo > 0 and self.shot_down == False:
            self.game_settings.ammo -= 1
            return Bullet(self.screen, self.game_settings, self.rect.centerx, self.rect.top)
        else:
            None
