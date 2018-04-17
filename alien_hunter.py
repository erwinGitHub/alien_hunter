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
    objects.append(background)
    
    #Create ship object
    ship = Ship(game_settings, screen)
    objects.append(ship)
    
    #Create group of alien ships
    aliens = Group()
    aliens.add(Alien(game_settings, screen, 10, 100))
    aliens.add(Alien(game_settings, screen, 140, 250))
    aliens.add(Alien(game_settings, screen, 270, 400))
    
    #Create group for bullets
    bullets = Group()
    
    while True:
        #Check events key down or key up
        gf.check_events(game_settings, screen, ship, bullets)
        
        #Refreash screen           
        gf.update_screen(game_settings, screen, objects, bullets, aliens)        

run_game()
