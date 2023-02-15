import sys
from time import sleep

import pygame

from bullet import Bullet
from alien import Alien


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


def update_screen(ai_settings, screen, ship, bullets, aliens):
    """update the image on the screen and switch to the new screen"""
    # redraw the screen after each loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # redraw aliens
    aliens.draw(screen)
    # redraw bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # display the latest drawn screen
    pygame.display.flip()


def check_bullet_alien_collisions(ai_settings, screen, ship, bullets, aliens):
    """
    check if any bullets hit the aliens.
    if so, then remove the corresponding bullet and alien
    """
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        # remove all existing bullets
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)


def update_bullets(ai_settings, screen, ship, bullets, aliens):
    bullets.update()
    # remove the disappeared bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets))
    check_bullet_alien_collisions(ai_settings, screen, ship, bullets, aliens)


def ship_hit(ai_settings, stats, screen, ship, bullets, aliens):
    """response to ship crashed by the aliens"""
    if stats.ships_left > 0:
        # decrease the left ships by 1
        stats.ships_left -= 1
        # empty the groups of both aliens and bullets
        aliens.empty()
        bullets.empty()
        # create a new fleet of aliens
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        # pause
        sleep(0.5)
    else:
        stats.game_active = False


def update_aliens(ai_settings, stats, screen, ship, bullets, aliens):
    """check whether there is any alien located in the edge and update all the aliens' positions"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # check collisions between aliens and the ship
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, bullets, aliens)

    # check if there is any aliens reaching the bottom of the screen
    check_aliens_bottom(ai_settings, stats, screen, ship, bullets, aliens)


def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        # create a bullet and add it to group bullets
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def create_fleet(ai_settings, screen, ship, aliens):
    """create an alien group"""
    # create an alien and calculate how many aliens each row can contain
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    for row_numer in range(number_rows):
        # create aliens for each row
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_numer)


def get_number_aliens_x(ai_settings, alien_width):
    # create an alien, and calculate how many aliens a row can contain
    # the span of two aliens is the width of one alien
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """calculate how many rows of aliens the screen can contain"""
    available_y_space = ai_settings.screen_height - ship_height - 4 * alien_height
    number_rows = int(available_y_space / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    # create an alien and add it to current row
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def check_fleet_edges(ai_settings, aliens):
    """when the alien approaches the edge"""
    for alien in aliens.sprites():
        if alien.check_edges() is True:
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """drop all the aliens and change their direction"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """check if any aliens reach the bottom of the screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # do with it like the ship is crashed by an alien
            ship_hit(ai_settings, stats, screen, ship, bullets, aliens)
            break
