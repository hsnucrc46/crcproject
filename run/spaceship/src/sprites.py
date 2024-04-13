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


class spaceship:
    """
    The player
    """

    def __init__(self, game):
        self.game = game
        self.health = lib.health
        self.ispaceship = pygame.transform.rotozoom(
            pygame.image.load("src/spaceship.png"), 0, 0.1
        )
        self.width = lib.width
        self.pos_x = self.width * 0.45
        self.pos_y = lib.height * 0.75
        self.rect = self.ispaceship.get_rect()
        self.rect.topleft = (self.pos_x, self.pos_y)
        self.direction_x = 0
        self.speed_x = 50

    def healthbar(self, screen):
        pygame.draw.rect(
            screen, (255, 0, 0), (50, 50, 200, 50)
        )  # Draw a background bar
        pygame.draw.rect(screen, (0, 255, 0), (50, 50, self.health * 20, 50))

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.direction_x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction_x = 1
        else:
            self.direction_x = 0

        self.pos_x += self.direction_x * self.speed_x
        if self.pos_x <= -200:
            self.pos_x = -200
        elif self.pos_x >= self.width - 350:
            self.pos_x = self.width - 350
        self.rect.topleft = (self.pos_x, self.pos_y)

    def draw(self, screen):
        self.game.screen.blit(self.ispaceship, (self.pos_x, self.pos_y))


class comet:
    """
    The enemy
    """

    def __init__(self, game):
        self.game = game
        self.icomet = pygame.transform.rotozoom(
            pygame.image.load("src/comet.png"), 0, 0.05
        )
        self.rect = self.icomet.get_rect()
        self.pos_x = randint(0, lib.width)
        self.pos_y = 0
        self.speed_y = 0
        self.acceleration_y = 9.8 / lib.fps
        self.rect.topleft = (self.pos_x, self.pos_y)

    def update(self):
        self.speed_y += self.acceleration_y
        self.pos_y += self.speed_y
        self.rect.topleft = (self.pos_x, self.pos_y)

    def draw(self):
        self.game.screen.blit(self.icomet, (self.pos_x, self.pos_y))
