import pygame

class Ship():
    """initialize ships and set their initial positions"""

    def __init__(self, screen, ai_settings):
        self.screen = screen
        self.ai_settings = ai_settings

        """load ship.bmp and get its external rectangle"""
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        """place each new ship in the bottom center of the screen"""
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        """enable storing float number in the property of the ship"""
        self.center = float(self.rect.centerx)

        """motivation flag"""
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """adapt the position of ship based on the motivation flag"""
        if self.moving_right == True and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left == True and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed_factor

        # update object rect based on self.center
        self.rect.centerx = self.center

    def blitme(self):
        """draw the ship at the specified location"""
        self.screen.blit(self.image, self.rect)
