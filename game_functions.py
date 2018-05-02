import sys
import pygame
from bullet import Bullet
from alien import Alien
from button import Button


def keydown_events(event, game_objects, ship, bullets):
    """Keydown events actions"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    
    if event.key == pygame.K_UP:
        ship.moving_up = True
    
    if event.key == pygame.K_DOWN:
        ship.moving_down = True
    
    if event.key == pygame.K_SPACE:
        bullet = ship.fire()
        if bullet != None:
            bullets.add(bullet)
            game_objects.add(bullet)
            
    if event.key == pygame.K_q:
        sys.exit()    

     
def keyup_events(event, ship):
    """Keyup events actions"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    
    if event.key == pygame.K_UP:
        ship.moving_up = False
    
    if event.key == pygame.K_DOWN:
        ship.moving_down = False


def mouse_event(buttons, game_stats):
    """Reaction on any mouse event.""" 
    mouse_pos = pygame.mouse.get_pos()
    mouse_buttons = pygame.mouse.get_pressed()
    for button in buttons.sprites():
        button.update_me(mouse_pos, mouse_buttons[0])
        if mouse_buttons[0] == 1 and button.action == "start":
            game_stats.game_started = True
            button.kill()
        elif mouse_buttons[0] == 1 and button.action == "stop":
            sys.exit()

def check_events(game_stats, game_objects, ship, bullets, buttons):
    """Reaction on events thrown by keyboard"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            keydown_events(event, game_objects, ship, bullets)
                
        elif event.type == pygame.KEYUP:
            keyup_events(event, ship)
            
        elif event.type == pygame.MOUSEMOTION:
            mouse_event(buttons, game_stats)
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_event(buttons, game_stats)
            
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_event(buttons, game_stats)
        

def create_fleet(screen, game_settings, game_objects, aliens):
    """Create fleet of aliens"""
    #Clculate how many aliens are possible to be load on panel in one row
    #Create temporary the alien object and retrieve width of this object
    a = Alien(screen, game_settings, 0, 0)
    alien_width = a.rect.width
    alien_height = a.rect.height
    number_of_aliens_in_row = int(game_settings.screen_width/(2*alien_width))
    number_of_rows = int(game_settings.screen_height/(3*alien_height))
    
    #Create rows
    y = 0
    for row_number in range(number_of_rows - 1):
        #Create one row of aliens
        x = alien_width
        for alien_number in range(number_of_aliens_in_row - 1):
            alien = Alien(screen, game_settings, x, y)
            game_objects.add(alien)
            aliens.add(alien)
            x += 2 * alien_width

        y += 2 * alien_height 
        

def create_start_buttons(screen, game_settings, game_objects, buttons):
    """Create buttons"""
    
    b = Button(screen, "Start Game", action="start")
    b.rect.centerx = int(game_settings.screen_width/2)
    b.rect.centery = int(game_settings.screen_height/2)
    game_objects.add(b)
    buttons.add(b)

def create_stop_button(screen, game_settings, game_objects, buttons):
    """Create buttons"""
    
    b = Button(screen, "Game Over", action="stop")
    b.rect.centerx = int(game_settings.screen_width/2)
    b.rect.centery = int(game_settings.screen_height/2)
    game_objects.add(b)
    buttons.add(b)
    
def check_collisions(screen, game_settings, game_stats, game_objects, ship, aliens, bullets, buttons):
    """Calculate collisions n game"""
        
    #Remove bullets outside screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullet.kill()
            
    #Check collisions between bullets and aliens. In case bullet colide
    #with alien then remove both
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for a in collisions.values():
            game_stats.points += len(a)

    #Check if any alien reached bottom
    for alien in aliens.sprites():
        if alien.check_bottom():
            create_stop_button(screen, game_settings, game_objects, buttons)
            game_stats.game_started = False
            break

    #Check if any alien collide with ship
    if pygame.sprite.spritecollideany(ship, aliens):
        create_stop_button(screen, game_settings, game_objects, buttons)
        game_stats.game_started = False
            
    
def update_screen(game_objects):
    """Update images on screen then flip screen"""
    
    #Update background
    game_objects.update()

    #Swith last modified screen
    pygame.display.flip()  
