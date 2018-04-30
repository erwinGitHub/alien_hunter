import sys
import pygame
from bullet import Bullet
from alien import Alien
from button import Button


def keydown_events(event, game_objects):
    """Keydown events actions"""
    if event.key == pygame.K_RIGHT:
        game_objects["ship"].moving_right = True
    
    if event.key == pygame.K_LEFT:
        game_objects["ship"].moving_left = True
    
    if event.key == pygame.K_UP:
        game_objects["ship"].moving_up = True
    
    if event.key == pygame.K_DOWN:
        game_objects["ship"].moving_down = True
    
    if event.key == pygame.K_SPACE:
        if len(game_objects["bullets"]) < 3:
            game_objects["bullets"].add(Bullet(game_objects))
    
    if event.key == pygame.K_q:
        sys.exit()    

     
def keyup_events(event, game_obects):
    """Keyup events actions"""
    if event.key == pygame.K_RIGHT:
        game_objects["ship"].moving_right = False
    
    if event.key == pygame.K_LEFT:
        game_objects["ship"].moving_left = False
    
    if event.key == pygame.K_UP:
        game_objects["ship"].moving_up = False
    
    if event.key == pygame.K_DOWN:
        game_objects["ship"].moving_down = False

def mouse_event(game_objects):
    """Reaction on any mouse event.""" 
    mouse_pos = pygame.mouse.get_pos()
    mouse_buttons = pygame.mouse.get_pressed()
    for button in game_objects["buttons"].sprites():
        button.update_me(mouse_pos, mouse_buttons[0])


def check_events(game_objects):
    """Reaction on events thrown by keyboard"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            keydown_events(event, game_objects)
                
        elif event.type == pygame.KEYUP:
            keyup_events(event, game_objects)
            
        elif event.type == pygame.MOUSEMOTION:
            mouse_event(game_objects)
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_event(game_objects)
            
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_event(game_objects)
        

def create_fleet(game_objects):
    """Create fleet of aliens"""
    #Clculate how many aliens are possible to be load on panel in one row
    #Create temporary the alien object and retrieve width of this object
    a = Alien(game_objects, 0, 0)
    alien_width = a.rect.width
    alien_height = a.rect.height
    number_of_aliens_in_row = int(game_objects["game_settings"].screen_width/(2*alien_width))
    number_of_rows = int(game_objects["game_settings"].screen_height/(3*alien_height))
    
    #Create rows
    y = 0
    for row_number in range(number_of_rows - 1):
        #Create one row of aliens
        x = alien_width
        for alien_number in range(number_of_aliens_in_row - 1):
            alien = Alien(game_objects, x, y)
            game_objects["aliens"].add(alien)
            x += 2 * alien_width

        y += 2 * alien_height 
        

def create_start_buttons(game_objects):
    """Create buttons"""
    
    b = Button(game_objects, "test button", 150, 100, 100, 50)
    game_objects["buttons"].add(b)
    
    
def update_screen(game_objects):
    """Update images on screen then flip screen"""
    
    #Remove bullets outside screen
    for b in game_objects["bullets"].copy():
        if b.rect.bottom <= 0:
            game_objects["bullets"].remove(b)

    #Check collisions between bullets and aliens. In case bullet colide
    #with alien then remove both
    collisions = pygame.sprite.groupcollide(game_objects["bullets"], 
                                            game_objects["aliens"], True, True)

    #Check if any alien reached bottom
    for alien in game_objects["aliens"]:
        if alien.check_bottom():
            print('You loose!!! ')
            game_objects["game_settings"].game_end = True
            break

    #Check if any alien collide with ship
    if pygame.sprite.spritecollideany(game_objects["ship"], game_objects["aliens"]):
        print('Ship was destroyed!!!')
        game_objects["game_settings"].game_end = True
        
    #Refresh objects on the screen
    for obj in game_objects.values():
        obj.update()
        obj.draw()
    
    #Swith last modified screen
    pygame.display.flip()  
    
