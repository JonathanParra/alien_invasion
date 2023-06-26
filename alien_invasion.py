import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """clase general para gestionar los recursos y el comportamiento del juego"""
    def __init__(self):
        """inicializar el juego y crea recursos"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width= self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("alien invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        #cambia el color de fondo


    def run_game(self):
        """inicia el bucle principal para el juego"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    def _fire_bullet(self):
        """crea una bala nueva y la añade al grupo de balas"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)


    def _check_events(self):
        # busca eventos de raton y teclado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            # mover la nave a la derecha.
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # mover la nave a la Izquierda.
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        # Redibuja la pantalla en cada paso por el bucle
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # hace visible la ultima pantalla dibujada.
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()

if __name__ == '__main__':
    #crea una instancia del juego y lo inicia.
    ai = AlienInvasion()
    ai.run_game()
