class GameStats:
    """track game statistics"""

    def __init__(self, ai_settings):
        """initialize statistics"""
        self.ships_left = None
        self.ai_settings = ai_settings
        self.reset_stats()
        # the game is inactive when it starts
        self.game_active = False
        self.score = 0
        self.level = 0
        # under no circumstances should the highest score be reset
        self.high_score = 0

    def reset_stats(self):
        """initialize the statistics that may change during the game run"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
