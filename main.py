import pygame

pygame.init()

# window configuration
RESOLUTION = (800, 600)
window = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption("CityRiot")

# image configuration
player_sprite = pygame.image.load("assets/sprites/player_character.png")
coin_sprite = pygame.image.load("assets/sprites/coin.png")
bullet_sprite = pygame.image.load("assets/sprites/bullet.png")

# scaling the sprites
player_sprite_scaled = pygame.transform.scale(player_sprite, (64, 64))
bullet_sprite_scaled = pygame.transform.scale(bullet_sprite, (16, 16))
coin_sprite_scaled = pygame.transform.scale(coin_sprite, (16, 16))

# rotating the sprites
player_sprite_rotated = pygame.transform.rotate(player_sprite_scaled, 5)

# flipping the sprites
player_sprite_flipped = pygame.transform.flip(player_sprite_scaled, True, False)

# color configuration
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# inserting characters in the screen
window.blit(player_sprite_scaled, (400, 300))
window.blit(bullet_sprite_scaled, (433, 300))
window.blit(coin_sprite_scaled, (370, 300))

window.blit(player_sprite_rotated, (120, 120))
window.blit(player_sprite_flipped, (200, 200))

# updates the screen
pygame.display.flip()

# main game loop
game_running = True

while (game_running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False






pygame.quit()


