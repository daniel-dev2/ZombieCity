import pygame


class Player:
    def __init__(self):
        self.sprite = pygame.image.load("assets/sprites/player_character.png")
        self.sprite = pygame.transform.scale(self.sprite, (64, 64))
        self.sprite_flipped = pygame.transform.flip(self.sprite, True, False)
        self.sprite_unflipped = pygame.transform.flip(self.sprite, False, False)
        self.rect = self.sprite.get_rect()
        self.direction = pygame.math.Vector2()
        self.position = pygame.math.Vector2(self.rect.center)
        self.speed = 1
        self.facing_left = False
        self.facing_right = False
        self.health = 10
        self.last_time_hit = pygame.time.get_ticks()
        self.hit_cooldown = 1000

        self.position.x = 336
        self.position.y = 236

    def move(self):
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        # player has gone out of horizontal bounds
        if self.position.x < -4.0:
            self.position.x = -4.0
            self.rect.centerx = self.position.x

        elif self.position.x > 740:
            self.position.x = 740
            self.rect.centerx = self.position.x

        # player has gone out of vertical bounds
        elif self.position.y < 124:
            self.position.y = 124
            self.rect.centery = self.position.y

        elif self.position.y > 536:
            self.position.y = 536
            self.rect.centery = self.position.y

        else:
            # horizontal movement
            self.position.x += self.direction.x * self.speed
            self.rect.centerx = self.position.x

            # vertical movement
            self.position.y += self.direction.y * self.speed
            self.rect.centery = self.position.y