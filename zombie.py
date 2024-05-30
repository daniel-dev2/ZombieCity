import pygame
import random


class Zombie:
    def __init__(self, speed):
        self.speed = speed
        self.sprite = pygame.image.load("assets/sprites/zombie.png")
        self.sprite = pygame.transform.scale(self.sprite, (64, 64))
        self.rect = self.sprite.get_rect()
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.hp = 4

    def spawn(self):
        LEFT_BORDER_X = (-20, 0)
        LEFT_BORDER_Y = (124, 630)

        BOTTOM_BORDER_X = (0, 800)
        BOTTOM_BORDER_Y = (630, 650)

        RIGHT_BORDER_X = (830, 850)
        RIGHT_BORDER_Y = (124, 630)

        spawn_area = random.randint(0, 2)

        # spawn in left border
        if spawn_area == 0:
            self.pos.x = random.randint(LEFT_BORDER_X[0], LEFT_BORDER_X[1])
            self.rect.centerx = self.pos.x

            self.pos.y = random.randint(LEFT_BORDER_Y[0], LEFT_BORDER_Y[1])
            self.rect.centery = self.pos.y

        # spawn in bottom border
        elif spawn_area == 1:
            self.pos.x = random.randint(BOTTOM_BORDER_X[0], BOTTOM_BORDER_X[1])
            self.rect.centerx = self.pos.x

            self.pos.y = random.randint(BOTTOM_BORDER_Y[0], BOTTOM_BORDER_Y[1])
            self.rect.centery = self.pos.y

        # spawn in right border
        else:
            self.pos.x = random.randint(RIGHT_BORDER_X[0], RIGHT_BORDER_X[1])
            self.rect.centerx = self.pos.x

            self.pos.y = random.randint(RIGHT_BORDER_Y[0], RIGHT_BORDER_Y[1])
            self.rect.centery = self.pos.y

    def move(self, player_position):
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
        # horizontal movement
        # TODO flip zombie sprites horizontally when facing the player
        if self.pos.x > player_position.x:
            self.direction.x = 1
            self.pos.x -= self.direction.x * self.speed
            self.rect.centerx = self.pos.x

        elif self.pos.x < player_position.x:
            self.direction.x = 1
            self.pos.x += self.direction.x * self.speed
            self.rect.centerx = self.pos.x

        # vertical movement
        if self.pos.y > player_position.y:
            self.direction.y = -1
            self.pos.y += self.direction.y * self.speed
            self.rect.centery = self.pos.y

        elif self.pos.y < player_position.y:
            self.direction.y = 1
            self.pos.y += self.direction.y * self.speed
            self.rect.centery = self.pos.y

    def collision(self, player):
        if self.rect.colliderect(player.rect):  # Use colliderect to check for collision
            now = pygame.time.get_ticks()
            if now - player.last_time_hit >= player.hit_cooldown:
                player.last_time_hit = now
                player.health -= 2


