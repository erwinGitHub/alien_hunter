import pygame
from pygame.time import Clock
from pygame.sprite import Group
from game_settings import Settings
from game_statistics import Stats
from background import Background
from ship import Ship
import game_functions as gf

def run_game():

    #Create some groups of objects
    game_objects = Group()
    bullets = Group()
    aliens = Group()
    buttons = Group()
    
    #Initialize game settings
    game_settings = Settings()
    
    #Initialize game statistics
    game_stats = Stats()
    
    #Pygame initiation, and establish screen  
    pygame.init()
    screen = pygame.display.set_mode((game_settings.screen_width, 
                        game_settings.screen_height))
    pygame.display.set_caption(game_settings.screen_title)
    
    #Create background object
    background = Background(screen, game_settings)
    game_objects.add(background)
    
    #Create ship object
    ship = Ship(screen, game_settings)
    game_objects.add(ship)
    
    #Create fleet of aliens then add them to game objects and aliens groups
    gf.create_fleet(screen, game_settings, game_objects, aliens)
    
    #Create buttons then ass them to game_objects and buttons groups
    gf.create_start_buttons(screen, game_settings, game_objects, buttons)
    
    #Create clock object
    clock = Clock()
    
    while game_stats.game_started:
        
        #Check events key down or key up
        gf.check_events(game_objects, ship, bullets, buttons)
        
        #Check collisions
        gf.check_collisions(game_stats, game_objects, ship, aliens, bullets)
        
        #Update screen           
        gf.update_screen(game_objects)

        #Wait certain time to achieve 40fps 
        clock.tick(40)

run_game()
