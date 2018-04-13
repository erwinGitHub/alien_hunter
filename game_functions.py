import sys
import pygame
from bullet import Bullet


def keydown_events(event, game_settings, screen, ship, bullets):
    """Keydown events actions"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(game_settings, screen, ship)
        bullets.add(new_bullet)

     
def keyup_events(event, ship):
    """Keyup events actions"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
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


def update_screen(game_settings, screen, objects, bullets):
    """Update images on screen then flip screen"""
    #Refresh objects on the screen
    for obj in objects:
        obj.update()
        obj.blitme()
    
    for bullet in bullets.sprites():
        bullet.draw_bullet()
        
    
    #Swith last modified screen
    pygame.display.flip()
