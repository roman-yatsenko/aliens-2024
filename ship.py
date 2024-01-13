import pygame


class Ship:
    """Клас для управління кораблем"""

    def __init__(self, ai_game):
        """Ініціалізує корабель та встановлює його початкову позицію"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Завантаження зображення коребля і отримання прямокутника
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        # Кожен новий корабель з'являється у нижньої частини екрану
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Рисує корабель в поточній позиції"""
        self.screen.blit(self.image, self.rect)
