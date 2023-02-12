import sys

import pygame

from bullet import Bullet

def check_events(ai_settings, screen, ship, bullets):
    """respond to keystroke and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        # move the ship to the right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # move the ship to the left
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        pygame.quit()
        sys.exit()

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_screen(ai_settings, screen, ship, bullets):
    """update the image on the screen and switch to the new screen"""
    # redraw the screen after each loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # redraw bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # display the latest drawed screen
    pygame.display.flip()

def update_bullets(bullets):
    bullets.update()
    # remove the disappeared bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets))

def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        # create a bullet and add it to group bullets
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)