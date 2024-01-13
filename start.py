import sys

import pygame


class AlienInvasion:
    """Клас для управління ресурсами та поведінкою гри"""

    def __init__(self):
        """Ініціалізує гру та створює ігрові ресурси"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        # Призначення коліру фону
        self.bg_color = (230, 230, 230)  # RGB

    def run_game(self):
        """Запуск основного циклу гри"""
        while True:
            # Відслідковування подій клавіфатури та миші
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # За кожної ітерації циклу перемалбовується екран
            self.screen.fill(self.bg_color)

            # Відображення останнього прорисованого екрану
            pygame.display.flip()


if __name__ == "__main__":
    # Створення екземпляру та запуск гри
    ai = AlienInvasion()
    ai.run_game()
