"""
File: sprites.py
Author: 
Email: hsnu.crc46th@gmail.com
Github: https://github.com/hsnucrc46
Description: Sprites(objects) declaration
"""


import pygame
import random
import src.lib as lib

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("player.png"), (lib.player_size, lib.player_size))
        self.rect = self.image.get_rect(center=(lib.SCREEN_WIDTH // 2, lib.SCREEN_HEIGHT // 2))
        self.health = 100

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

    def draw_health_bar(surface, x, y, health):
        BAR_LENGTH = 100
        BAR_HEIGHT = 10
        fill = (health / 100) * BAR_LENGTH
        outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
        fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
        pygame.draw.rect(surface, "red", fill_rect)
        pygame.draw.rect(surface, "white", outline_rect, 2)


class Stone(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("stone.png"), (lib.STONE_SIZE, lib.STONE_SIZE))
        self.rect = self.image.get_rect()
        self.direction = random.choice(["right", "left", "up", "down"])
        if self.direction == "right":
            self.rect.x = -lib.stone_size
            self.rect.y = random.randint(0, lib.height - lib.stone_size)
            self.speed_x = lib.stone_speed
            self.speed_y = 0
        elif self.direction == "left":
            self.rect.x = lib.width
            self.rect.y = random.randint(0, lib.height - lib.stone_size)
            self.speed_x = -lib.stone_speed
            self.speed_y = 0
        elif self.direction == "up":
            self.rect.x = random.randint(0, lib.width - lib.stone_size)
            self.rect.y = lib.height
            self.speed_x = 0
            self.speed_y = -lib.stone_speed
        elif self.direction == "down":
            self.rect.x = random.randint(0, lib.width - lib.stone_size)
            self.rect.y = -lib.stone_size
            self.speed_x = 0
            self.speed_y = lib.stone_speed

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.right < 0 or self.rect.left > lib.width or self.rect.bottom < 0 or self.rect.top > lib.height:
            self.kill()
