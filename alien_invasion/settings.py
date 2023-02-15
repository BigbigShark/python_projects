class Settings:
    """a class to store all the settings for alien_invasion"""

    def __init__(self):
        """initialize the game settings"""
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
        self.bullets_allowed = 3

        """settings for the alien"""
        self.alien_speed_factor = 0.3
        self.fleet_drop_speed = 10
        # fleet_direction为1表示右移，为-1表示向左移
        self.fleet_direction = 1  # so smart!
