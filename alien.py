import pygame
from pygame.sprite import Sprite
import random

class Alien(Sprite):
    """Class which describes one alien ship"""
    
    def __init__(self, screen, game_settings, x, y):
        """init object settings"""
        super().__init__()
        
        self.screen = screen
        self.game_settings = game_settings
        self.screen_rect = self.screen.get_rect()
        
        #load alien images
        self.images = []
        for image in self.game_settings.alien_images:
            self.images.append(pygame.image.load(image))
            
        self.rect = self.images[0].get_rect()
        self.shot_down = False
        self.current_image = 0
        
        #Set initial position for alien ship
        self.rect.x = x
        self.rect.y = y
        
        #Save precission position of alien ship
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        #Set movement dirrection (left = +1 or right = -1)
        self.movement_dirrection = random.choice([-1, 1])
        
        #Set current drop factor
        self.current_drop_factor = 0.0
        
        #speed and drop factors
        self.speed_factor = random.randint(1, self.game_settings.alien_speed_factor)
        self.drop_factor = random.randint(50, self.game_settings.alien_drop_factor)
        
        
    
    def check_edges(self):
        """Method which checks if alien is near border. If so then 
        change movement dirrection"""  
        if self.rect.right >= self.screen_rect.right:
            self.movement_dirrection = -1
            self.current_drop_factor = self.drop_factor
        
        if self.rect.left <= self.screen_rect.left:
            self.movement_dirrection = 1    
            self.current_drop_factor = self.drop_factor
    
    
    def check_bottom(self):
        """Method which checks if alien reached bottom f screen."""  
        if self.rect.bottom >= self.screen_rect.bottom:
            return True
        else:
            return False

    def draw(self):
        if self.shot_down:
            self.current_image += 1
        
        if self.current_image >= len(self.images):
            self.kill()
        else:
            self.screen.blit(self.images[self.current_image], self.rect)

    def update(self):
        """Update alien ship position on screen""" 
        
        self.check_edges()
        self.x += self.speed_factor * self.movement_dirrection
        
        if self.current_drop_factor > 0:
            self.y += self.speed_factor
            self.current_drop_factor -= self.speed_factor
      
        self.rect.x = self.x      
        self.rect.y = self.y      
        self.draw()
