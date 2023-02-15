class GameStats:
    """track game statistics"""

    def __init__(self, ai_settings):
        """initialize statistics"""
        self.ships_left = None
        self.ai_settings = ai_settings
        self.reset_stats()
        # the game is activated when it starts
        self.game_active = True

    def reset_stats(self):
        """initialize the statistics that may change during the game run"""
        self.ships_left = self.ai_settings.ship_limit
        