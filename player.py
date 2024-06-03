import pygame


class Player:

    def __init__(self):
        # player image configuration
        self.sprite = pygame.image.load("assets/sprites/player_character.png")
        self.sprite = pygame.transform.scale(self.sprite, (64, 64))
        self.sprite_flipped = pygame.transform.flip(self.sprite, True, False)
        self.sprite_unflipped = pygame.transform.flip(self.sprite, False, False)

        # player movement configuration
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

        # bullet configuration
        self.bullet_sprite = pygame.image.load("assets/sprites/bullet.png")
        self.bullet_sprite = pygame.transform.scale(self.bullet_sprite, (16, 16))
        self.bullet_sprite_flipped = pygame.transform.flip(self.bullet_sprite, True, False)
        self.bullet_sprite_unflipped = pygame.transform.flip(self.bullet_sprite, False, False)
        self.bullet_rect = self.bullet_sprite.get_rect()
        self.bullet_pos = pygame.math.Vector2(self.bullet_rect.center)
        self.bullet_facing_left = False
        self.bullet_facing_right = False
        self.bullet_active = False

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

    def shoot(self, zombie) -> None:
        if not self.bullet_active:
            # set bullet's initial position
            self.bullet_pos.x = self.position.x + (64 if self.bullet_facing_right else -16)
            self.bullet_pos.y = self.position.y + 29
            self.bullet_active = True

        if self.bullet_facing_right:
            self.bullet_pos.x += 1.5
        else:
            self.bullet_pos.x -= 1.5

        self.bullet_rect.centerx = self.bullet_pos.x

        # bullet has gone out of horizontal bounds
        if self.bullet_pos.x > 784 or self.bullet_pos.x < -16:
            self.bullet_active = False

        if self.bullet_rect.colliderect(zombie.rect):
            zombie.hp -= 2
            self.bullet_active = False

    def set_bullet_direction(self, facing_left: bool, facing_right: bool) -> None:
        self.bullet_facing_left = facing_left
        self.bullet_facing_right = facing_right
