import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from ship import Ship
import game_functions as gf


def run_game():
    # initialize the game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    # create an instance to store game statistics
    stats = GameStats(ai_settings)

    # create a ship
    ship = Ship(ai_settings, screen)
    # create a group to store bullets
    bullets = Group()
    # create alien fleet
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # start the main loop of the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)

        if stats.game_active is True:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, bullets, aliens)
            gf.update_aliens(ai_settings, stats, screen, ship, bullets, aliens)

        gf.update_screen(ai_settings, screen, ship, bullets, aliens)


if __name__ == "__main__":
    run_game()
