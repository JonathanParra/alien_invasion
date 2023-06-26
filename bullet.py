import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """clase para gestionar las balas disparadas de la nave"""

    def __init__(self, ai_game):
        """crea un objeto para la bala en la posición actual de la nave"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        """crea un rectangulo para la bala en (0, 0 ) y luego estabece la posición correcta """
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Guarda la posición de la bala como valor decimal
        self.y = float(self.rect.y)

    def update(self):
        """mueve la bala hacia arriba por la pantalla"""

        #Actualiza la posición decimal de la bala.
        self.y -= self.settings.bullet_speed

        #actualiza la posición del rectangulo.
        self.rect.y = self.y

    def draw_bullet(self):
        """dibuja la bala en la pantalla."""
        pygame.draw.rect(self.screen, self.color, self.rect)