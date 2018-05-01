import pygame
from pygame.sprite import Group
from game_settings import Settings
from background import Background
from ship import Ship
import game_functions as gf

def run_game():

    #Create game_objects dictionary
    game_objects = {}
    
    #Initialize game settings
    game_settings = Settings();
    
    #Pygame initiation, and establish screen  
    pygame.init()
    screen = pygame.display.set_mode((game_settings.screen_width, 
                        game_settings.screen_height))
    pygame.display.set_caption(game_settings.screen_title)
    
    #Create background object
    game_objects["background"] = Background(screen, game_settings)
    
    #Create ship object
    game_objects["ship"] = Ship(screen, game_settings)
    
    #Create group of alien ships
    game_objects["aliens"] = Group()
    gf.create_fleet(screen, game_settings, game_objects)
    
    #Create group for bullets
    game_objects["bullets"] = Group()
    
    #Create group of buttons
    game_objects["buttons"] = Group()
    gf.create_start_buttons(screen, game_settings, game_objects)
    
    while True:
        #Check events key down or key up
        gf.check_events(game_objects)
        
        #Refreash screen           
        gf.update_screen(screen, game_settings, game_objects)
        
        #Chack if end game
        if game_settings.game_end:
            break        

run_game()
