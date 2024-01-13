import sys

import pygame
from tomlkit import key

from settings import Settings
from ship import Ship


class AlienInvasion:
    """Клас для управління ресурсами та поведінкою гри"""

    def __init__(self):
        """Ініціалізує гру та створює ігрові ресурси"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Запуск основного циклу гри"""
        while True:
            # Відслідковування подій клавіфатури та миші
            self._check_events()
            self.ship.update()
            # За кожної ітерації циклу перемальовується екран
            self._update_screen()

    def _check_events(self):
        """Обробляє натиснеяння клавіш та події миші"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # Переміщуємо корабель праворуч
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False

    def _update_screen(self):
        """ "Оновлює зображення на екрані та відображає новий екран"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # Відображення останнього прорисованого екрану
        pygame.display.flip()


if __name__ == "__main__":
    # Створення екземпляру та запуск гри
    ai = AlienInvasion()
    ai.run_game()
