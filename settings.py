class Settings:
    """Клас для збереження всін налаштувань гри"""

    def __init__(self):
        """Ініціалізує налаштування гри"""
        # Параметри екрану
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Параметри корабля
        self.ship_limit = 3

        # Параметри снаряду
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bulets_allowed = 3

        # Параметри прибульців
        self.fleet_drop_speed = 10

        # Темпи прискорення гри
        self.speedup_scale = 1.1

        self.initialyze_dynamic_settings()

    def initialyze_dynamic_settings(self):
        """Ініціалізує налаштування, що змінюються по ходу гри"""
        self.ship_speed = 1.5
        self.bullet_speed = 1.5
        self.alien_speed = 1.0

        # fleet_direction = 1 якщо флот рухається праворуч, -1 - ліворуч
        self.fleet_direction = 1

    def increase_speed(self):
        """Збільшує налаштування швидкості"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
