import pygame
import random
from zombie import Zombie

pygame.init()

# window configuration
RESOLUTION = (800, 600)
window = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption("ZombieCity")

# image configuration
player_sprite = pygame.image.load("assets/sprites/player_character.png")
coin_sprite = pygame.image.load("assets/sprites/coin.png")
bullet_sprite = pygame.image.load("assets/sprites/bullet.png")
zombie_sprite = pygame.image.load("assets/sprites/zombie.png")
heavy_sprite = pygame.image.load("assets/sprites/heavy_zombie.png")
background_image = pygame.image.load("assets/sprites/city_background.png")
icon = pygame.image.load("assets/sprites/icon.png")
pygame.display.set_icon(icon)

# scaling the sprites
player_sprite_scaled = pygame.transform.scale(player_sprite, (64, 64))
bullet_sprite_scaled = pygame.transform.scale(bullet_sprite, (16, 16))
coin_sprite_scaled = pygame.transform.scale(coin_sprite, (16, 16))

# rotating the sprites
player_sprite_rotated = pygame.transform.rotate(player_sprite_scaled, 5)

# flipping the sprites
player_sprite_flipped = pygame.transform.flip(player_sprite_scaled, True, False)
player_sprite_unflipped = pygame.transform.flip(player_sprite_scaled, False, False)

zombie_sprite_flipped = pygame.transform.flip(zombie_sprite, True, False)
zombie_sprite_unflipped = pygame.transform.flip(zombie_sprite, False, False)

# color configuration
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# inserting characters in the screen
# window.blit(player_sprite_scaled, (400, 300))
# window.blit(bullet_sprite_scaled, (433, 300))
# window.blit(coin_sprite_scaled, (370, 300))

# window.blit(player_sprite_rotated, (120, 120))
# window.blit(player_sprite_flipped, (200, 200))

# player configuration
# player_x = 368
# player_y = 268
player_rect = player_sprite_scaled.get_rect()
player_direction = pygame.math.Vector2()
player_position = pygame.math.Vector2(player_rect.center)
player_speed = 1
player_facing_left = False
player_facing_right = False

# initial player position
player_position.x = 336
player_position.y = 236


def move(pos, direction, speed, rect):
    if direction.magnitude() > 0:
        direction = direction.normalize()

    # player has gone out of horizontal bounds
    if pos.x < -4.0:
        pos.x = -4.0
        rect.centerx = pos.x
    elif pos.x > 740:
        pos.x = 740
        rect.centerx = pos.x
    # player has gone out of vertical bounds
    elif pos.y < 124:
        pos.y = 124
        rect.centery = pos.y
    elif pos.y > 536:
        pos.y = 536
        rect.centery = pos.y
    else:
        # horizontal movement
        pos.x += direction.x * speed
        rect.centerx = pos.x

        # vertical movement
        pos.y += direction.y * speed
        rect.centery = pos.y


zombie_rect = zombie_sprite.get_rect()
heavy_rect = heavy_sprite.get_rect()

zombie1 = Zombie(0.3, zombie_sprite, zombie_rect, pygame.math.Vector2(), pygame.math.Vector2(zombie_rect.center))
zombie2 = Zombie(0.4, zombie_sprite, zombie_rect, pygame.math.Vector2(), pygame.math.Vector2(zombie_rect.center))
zombie3 = Zombie(0.5, zombie_sprite, zombie_rect, pygame.math.Vector2(), pygame.math.Vector2(zombie_rect.center))
zombie4 = Zombie(0.6, zombie_sprite, zombie_rect, pygame.math.Vector2(), pygame.math.Vector2(zombie_rect.center))
zombie5 = Zombie(0.5, zombie_sprite, zombie_rect, pygame.math.Vector2(), pygame.math.Vector2(zombie_rect.center))
zombie6 = Zombie(0.3, zombie_sprite, zombie_rect, pygame.math.Vector2(), pygame.math.Vector2(zombie_rect.center))
zombie7 = Zombie(0.2, heavy_sprite, heavy_rect, pygame.math.Vector2(), pygame.math.Vector2(heavy_rect.center))

wave1 = [zombie1, zombie2, zombie3, zombie4, zombie5, zombie6, zombie7]

for zombie in wave1:
    zombie.spawn()


# main game loop
game_running = True

while game_running:
    window.blit(background_image, (0, 0))
    for zombie in wave1:
        zombie.move(player_position)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    # player movement
    keys = pygame.key.get_pressed()
    # UP and DOWN
    if keys[pygame.K_w]:
        player_direction.y = -1

    elif keys[pygame.K_s]:
        player_direction.y = 1

    else:
        player_direction.y = 0

    # LEFT and RIGHT
    if keys[pygame.K_a]:
        player_facing_left = True
        player_direction.x = -1

    elif keys[pygame.K_d]:
        player_facing_right = True
        player_direction.x = 1

    else:
        player_direction.x = 0

    move(player_position, player_direction, player_speed, player_rect)

    # flipping the player horizontally
    if player_facing_left:
        player_sprite_scaled = player_sprite_flipped
        player_facing_left = False

    if player_facing_right:
        player_sprite_scaled = player_sprite_unflipped
        player_facing_right = False

    for zombie in wave1:
        window.blit(zombie.sprite, zombie.pos)

    #print(f'Zombie1 position: {zombie1.pos.x}, {zombie1.pos.y}')
    #print(f'Zombie2 position: {zombie2.pos.x}, {zombie2.pos.y}')
    window.blit(player_sprite_scaled, player_position)
    pygame.display.flip()

pygame.quit()
