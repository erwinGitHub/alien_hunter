import sys
import pygame
from bullet import Bullet
from alien import Alien


def keydown_events(event, game_settings, screen, ship, bullets):
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
        bullets.add(Bullet(game_settings, screen, ship))
    
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


def check_events(game_settings, screen, ship, bullets):
    """Reaction on events thrown by keyboard"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            keydown_events(event, game_settings, screen, ship, bullets)
                
        elif event.type == pygame.KEYUP:
            keyup_events(event, ship)


def create_fleet(game_settings, screen, aliens):
    """Create fleet of aliens"""
    #Clculate how many aliens are possible to be load on panel in one row
    #Create temporary the alien object and retrieve width of this object
    a = Alien(game_settings, screen, 0, 0)
    alien_width = a.rect.width
    alien_height = a.rect.height
    number_of_aliens_in_row = int(game_settings.screen_width/(2*alien_width))
    number_of_rows = int(game_settings.screen_height/(2*alien_height))
    
    #Create rows
    y = 0
    for row_number in range(number_of_rows - 1):
        #Create one row of aliens
        x = alien_width
        for alien_number in range(number_of_aliens_in_row - 1):
            alien = Alien(game_settings, screen, x, y)
            aliens.add(alien)
            x += 2 * alien_width

        y += 2 * alien_height 
        

def update_screen(game_settings, screen, objects, bullets, aliens):
    """Update images on screen then flip screen"""
    #Refresh objects on the screen
    for obj in objects:
        obj.update()
        obj.draw_me()

    #Remove bullets outside screen
    for b in bullets.copy():
        if b.rect.bottom <= 0:
            bullets.remove(b)

    #Update position of all bullets. To do this I use update method
    #Method update is run automatically for all sprites
    bullets.update()
    
    #Check collisions between bullets and aliens. In case bullet colide
    #with alien then remove both
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    
    #Update position of all aliens. To do this I use update method
    #Method update is run automatically for all sprites
    aliens.update()
    
    #Here I need to loop through all sprites because I need to draw all 
    #bullets. The Group class do not support draw_me method!
    for bullet in bullets.sprites():
        bullet.draw_me()
    
    
    #Here I draw aliens. I do it by run method draw for all sprites
    aliens.draw(screen)
    #Swith last modified screen
    pygame.display.flip()
