import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """Клас для управління ресурсами та поведінкою гри"""

    def __init__(self):
        """Ініціалізує гру та створює ігрові ресурси"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Запуск основного циклу гри"""
        while True:
            # Відслідковування подій клавіфатури та миші
            self._check_events()
            self.ship.update()
            self._update_bullets()

            # За кожної ітерації циклу перемальовується екран
            self._update_screen()

    def _check_events(self):
        """Обробляє натиснеяння клавіш та події миші"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Реагує на натиснення клавіш"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Реагує на відпускання клавіш"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _create_fleet(self):
        """Створення флоту прибульців"""
        # Створення прибульця і визначення кількості прибульців в ряду
        alien = Alien(self)
        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - 2 * alien_width
        number_aliens_x = available_space_x // (2 * alien_width)

        # Створення першого ряду прибульців
        for alien_number in range(number_aliens_x):
            # Створення прибульці і розміщення його в ряду
            alien = Alien(self)
            alien.x = alien_width + 2 * alien_width * alien_number
            alien.rect.x = alien.x
            self.aliens.add(alien)

    def _fire_bullet(self):
        """Створює новий снаряд та додає його до групи bullets"""
        if len(self.bullets) < self.settings.bulets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Оновлює позиції снарядів"""
        self.bullets.update()

        # Видалення снарядів, що вилетіли за край екрану
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_screen(self):
        """Оновлює зображення на екрані та відображає новий екран"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Відображення останнього прорисованого екрану
        pygame.display.flip()


if __name__ == "__main__":
    # Створення екземпляру та запуск гри
    ai = AlienInvasion()
    ai.run_game()
