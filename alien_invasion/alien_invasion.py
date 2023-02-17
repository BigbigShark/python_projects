import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
import game_functions as gf
from scoreboard import Scoreboard


def run_game():
    # initialize the game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    # create play button
    play_button = Button(ai_settings, screen, "Play")

    # create an instance to store game statistics
    stats = GameStats(ai_settings)
    # create an instance to store game statistics and create a scoreboard
    sb = Scoreboard(ai_settings, stats, screen)

    # create a ship
    ship = Ship(ai_settings, screen)
    # create a group to store bullets
    bullets = Group()
    # create alien fleet
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # start the main loop of the game
    while True:
        gf.check_events(ai_settings, stats, screen, sb, ship, bullets, aliens, play_button)

        if stats.game_active is True:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, bullets, aliens)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, bullets, aliens)

        gf.update_screen(ai_settings, screen, stats, sb, ship, bullets, aliens, play_button)


if __name__ == "__main__":
    run_game()
