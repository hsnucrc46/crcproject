"""
File: sprites.py
Author: Crystal Diamond, Oliver Tzeng, 314hello
Email: hsnu.crc46th@gmail.com
Github: https://github.com/hsnucrc46
Description: Sprites(objects) declaration
"""

import pygame
import random
import src.lib as lib


class player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.height = lib.height
        self.health = lib.max_health
        self.width = lib.width
        self.player_size = 50
        self.iplayer = pygame.transform.scale(
            pygame.image.load("src/player.png"), (self.player_size, self.player_size)
        )
        self.rect = self.iplayer.get_rect(center=(self.width // 2, self.height // 2))

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

    def draw(self):
        self.game.screen.blit(self.ispaceship, (self.pos_x, self.pos_y))


class comet(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.comet_size = 30
        self.icomet = pygame.transform.scale(
            pygame.image.load("src/comet.png"),
            (self.comet_size, self.comet_size),
        )
        self.rect = self.icomet.get_rect()
        self.height = lib.height
        self.width = lib.width
        self.direction = random.choice(lib.directions)
        self.comet_speed = 10
        match self.direction:
            case "right":
                self.rect.x = -self.comet_size
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
                self.rect.y = -self.comet_size
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
    
    def draw(self):
        self.game.screen.blit(self.icomet, (self.pos_x, self.pos_y))