import pygame


class PowerUps:
    def __init__(self):
        self.sprite = pygame.image.load("assets/sprites/medkit.png")
        self.rect = self.sprite.get_rect()

    def effect(self):
        # TODO implement this
        pass
