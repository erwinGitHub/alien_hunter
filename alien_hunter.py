import pygame
from pygame.sprite import Group
from game_settings import Settings
from background import Background
from ship import Ship
from screen import Screen
import game_functions as gf

def run_game():

    #Create game_objects dictionary
    game_objects = {}
    
    #Initialize game settings
    game_settings = Settings();
    game_objects["game_settings"] = game_settings
    
    #Pygame initiation, and establish screen  
    pygame.init()
    screen = Screen(game_objects)
    pygame.display.set_caption(game_settings.screen_title)
    game_objects["screen"] = screen
    
    #Create background object
    background = Background(game_objects)
    game_objects["background"] = background
    
    #Create ship object
    ship = Ship(game_objects)
    game_objects["ship"] = ship
    
    #Create group of alien ships
    aliens = Group()
    game_objects["aliens"] = aliens
    gf.create_fleet(game_objects)
    
    #Create group for bullets
    bullets = Group()
    game_objects["bullets"] = bullets
    
    #Create group of buttons
    buttons = Group()
    game_objects["buttons"] = buttons
    gf.create_start_buttons(game_objects)
    
    while True:
        #Check events key down or key up
        gf.check_events(game_objects)
        
        #Refreash screen           
        gf.update_screen(game_objects)
        
        #Chack if end game
        if game_settings.game_end:
            break        

run_game()
