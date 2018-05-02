import pygame
from pygame.time import Clock
from pygame.sprite import Group
from game_settings import Settings
from game_statistics import Stats
from background import Background
from ship import Ship
from label import Label
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
    
    #Some statistics labels
    level = Label(screen, "level: " + str(game_stats.level), 10, 10)
    game_objects.add(level)

    ammo = Label(screen, "ammo: " + str(ship.game_settings.ammo), 200, 10)
    game_objects.add(ammo)

    points = Label(screen, "score: " + str(game_stats.points), 400, 10)
    game_objects.add(points)

    #Update screen           
    gf.update_screen(game_objects)

    while True:
        if len(aliens) == 0:
            game_stats.level += 1
            game_settings.alien_speed_factor += 1
            game_settings.ammo = game_settings.initial_ammo
            #Create fleet of aliens then add them to game objects and aliens groups
            gf.create_fleet(screen, game_settings, game_objects, aliens)
        
        #Check events key down or key up
        gf.check_events(game_stats, game_objects, ship, bullets, buttons)
    
        level.text = "level: " + str(game_stats.level)
        ammo.text = "ammo: " + str(ship.game_settings.ammo)
        points.text = "score: " + str(game_stats.points)
        
        if game_stats.game_started:
            #Check collisions
            gf.check_collisions(screen, game_settings, game_stats, game_objects, ship, aliens, bullets, buttons)
        
            #Update screen           
            gf.update_screen(game_objects)

        #Wait certain time to achieve 40fps 
        clock.tick(40)

run_game()
