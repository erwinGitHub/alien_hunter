import pygame
from pygame.sprite import Group
from game_settings import Settings
from background import Background
from ship import Ship
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
    gf.create_fleet(game_settings, screen, aliens)
    
    #Create group for bullets
    bullets = Group()
    
    while True:
        #Check events key down or key up
        gf.check_events(game_settings, screen, ship, bullets)
        
        #Refreash screen           
        gf.update_screen(game_settings, screen, objects, bullets, aliens)
        
        #Chack if end game
        if game_settings.game_end:
            break        


game = input('Start Game (y/n)?:')
while game == 'y':
    run_game()
    print('\n\nGAME OVER!')
    game = input('Would You like to play once again (y/n)?:')
