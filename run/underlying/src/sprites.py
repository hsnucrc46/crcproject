"""
File: sprites.py
Author: Crystal Diamond, Oliver Tzeng, 314hello
Email: hsnu.crc46th@gmail.com
Github: https://github.com/hsnucrc46
Description: Sprites(objects) declaration
"""

from random import randint

import pygame
import src.lib as lib


class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.height = lib.height
        self.health = lib.max_health
        self.width = lib.width
        self.player_size = 50
        self.iplayer = pygame.transform.scale(
            pygame.image.load("src.player.png"), (self.player_size, self.player_size)
        )
        self.rect = self.iplayer.get_rect(center=(self.width // 2, self.height // 2))

    def update(self):
        self.rect.center = pygame.mouse.get_pos()


class comet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.icomet = pygame.transform.scale(
            pygame.image.load("src.comet.png"),
            (self.self.comet_size, self.self.comet_size),
        )
        self.rect = self.icomet.get_rect()
        self.height = lib.height
        self.width = lib.width
        self.direction = lib.direction
        self.comet_size = 30
        self.comet_speed = 10
        match self.direction:
            case "right":
                self.rect.x = 0 - self.comet_size
                self.rect.y = random.randint(0, self.height - self.comet_size)
                self.speed_x = self.comet_speed
                self.speed_y = 0
            case "left":
                self.rect.x = self.width
                self.rect.y = random.randint(0, self.height - self.comet_size)
                self.speed_x = -self.comet_speed
                self.speed_y = 0
            case "up":
                self.rect.x = random.randint(0, self.width - self.comet_size)
                self.rect.y = self.height
                self.speed_x = 0
                self.speed_y = -self.comet_speed
            case "down":
                self.rect.x = random.randint(0, self.width - self.comet_size)
                self.rect.y = 0 - self.comet_size
                self.speed_x = 0
                self.speed_y = self.comet_speed

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if (
            self.rect.right < 0
            or self.rect.left > lib.width
            or self.rect.bottom < 0
            or self.rect.top > lib.height
        ):
            self.kill()
