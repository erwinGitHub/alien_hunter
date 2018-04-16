import pygame
from pygame.sprite import Group
from game_settings import Settings
from background import Background
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
    #Pygame initiation, create Settings object and set screen 
    pygame.init()
    game_settings = Settings();
    screen = pygame.display.set_mode(
            (game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption(game_settings.screen_title)
    
    #Create list of objects
    objects = []
    
    #Create background object
    background = Background(game_settings, screen)
    
    #Create ship object
    ship = Ship(game_settings, screen)
    
    #Createalien ship
    alien = Alien(game_settings, screen)
    
    #Create group for bullets
    bullets = Group()
    
    #Add game objects to list
    objects.append(background)
    objects.append(ship)
    objects.append(alien)
    
    while True:
        gf.check_events(game_settings, screen, ship, bullets)
        
        #Remove bullets outside screen
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        
        #Refreash screen           
        gf.update_screen(game_settings, screen, objects, bullets)        

run_game()
