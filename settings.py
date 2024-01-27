class Settings:
    """Клас для збереження всін налаштувань гри"""

    def __init__(self):
        """Ініціалізує налаштування гри"""
        # Параметри екрану
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Параметри корабля
        self.ship_speed = 1.5

        # Параметри снаряду
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bulets_allowed = 3

        # Параметри прибульців
        self.alien_speed = 1.0
