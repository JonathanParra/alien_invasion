import pygame

class Ship:
    """clase para gestionar la Nave."""
    def __init__(self, ai_game):
        """inicializa la nave y configura su posición inicial."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #Carga la imagen de la nave y obtiene su rect.
        self.image = pygame.image.load('img/ship.bmp')
        self.rect = self.image.get_rect()

        #coloca inicialmente cada nave nueva en el centro de la parte inferior de la pantalla.
        self.rect.midbottom = self.screen_rect.midbottom
        #guarda un valor decimal para la posición horizontal de la nave.
        self.x = float(self.rect.x)
        # bandera de movimiento
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Actualiza la posicion de la nave en función de la bandera de movimiento"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #Actualiza el objeto rect de self.x
        self.rect.x = self.x

    def blitme(self):
        """dibuja la nave en su ubicación actual."""
        self.screen.blit(self.image, self.rect)

