import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """a class representing a single alien"""

    def __init__(self, ai_settings, screen):
        """initialize the alien and set its original position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load the image of the alien and set properties of its rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # each alien is in the top-left corner at the beginning
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the accurate position of the alien
        self.x = float(self.rect.x)

    def blitme(self):
        """draw the alien at the specified location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """move the alien to the right or to the left"""
        self.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """if the alien reaches the edge of the screen, return True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
