class Settings:
    """a class to store all the settings for alien_invasion"""

    def __init__(self):
        """initialize static settings of the game"""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (220, 220, 220)

        """settings for the ship"""
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        """settings for the bullet"""
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        """settings for the alien"""
        self.alien_speed_factor = 0.3
        self.fleet_drop_speed = 10

        self.fleet_direction = 1  # so smart!

        # speed the game
        self.speedup_scale = 1.1
        # increase the alien points
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """initialize the game as level goes up"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.5

        # fleet direction, 1 means to the right, -1 means to the left
        self.fleet_direction = 1

        # keep the score
        self.alien_points = 50

    def increase_speed(self):
        """accelerate the alien speed and increase the alien point"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
