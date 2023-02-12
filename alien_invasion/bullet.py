import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """a class to manage bullets from the ship"""

    def __init__(self, ai_settings, screen, ship):
        """create a bullet object at the location of the ship"""
        super(Bullet, self).__init__()
        self.screen = screen

        # create a rectangle representing the bullet and set the right position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # store the position of the bullet in float bumber
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """move the bullet upward"""
        # update the float value of the bullet position
        self.y -= self.speed_factor
        # update the rect position representing the bullet
        self.rect.y = self.y

    def draw_bullet(self):
        """draw the bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)