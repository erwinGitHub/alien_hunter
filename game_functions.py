import sys
import pygame
from bullet import Bullet


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

    #Update position of all bullets and aliens. To do this I use update method
    #Method update is run automatically for all sprites
    bullets.update()
    aliens.update()
    
    #Here I need to loop through all sprites because I need to draw all 
    #bullets. The Group class do not support draw_me method!
    for bullet in bullets.sprites():
        bullet.draw_me()
    
    
    #Here I draw aliens. I do it by run bethod draw for all sprites
    aliens.draw(screen)
    #Swith last modified screen
    pygame.display.flip()
