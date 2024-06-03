import pygame
from player import Player


class Bullet:
    def __init__(self):
        self.sprite = pygame.image.load("assets/sprites/bullet.png")
        self.sprite = pygame.transform.scale(self.sprite, (16, 16))
        self.sprite_flipped = pygame.transform.flip(self.sprite, True, False)
        self.sprite_unflipped = pygame.transform.flip(self.sprite, False, False)
        self.rect = self.sprite.get_rect()
        self.pos = pygame.math.Vector2(self.rect.center)
        # TODO implement bullet class
