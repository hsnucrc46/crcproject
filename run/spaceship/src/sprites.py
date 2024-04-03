"""
File: sprites.py
Author: Oliver Tzeng
Email: hsnu.crc46th@gmail.com
Github: https://github.com/hsnucrc46
Description: Sprites(objects) declaration
"""

from random import randint
import src.lib
import pygame


class rabbit:
    """
    The player
    """
    def __init__(self, game):
        self.game = game
        self.pos_x = src.lib.width * 0.45
        self.pos_y = src.lib.height * 0.75
        self.speed_x = 50
        self.direction_x = 0
        self.irabbit = pygame.image.load("src/rabbit.png")
        self.rect = self.irabbit.get_rect()
        self.rect.topleft = (self.pos_x, self.pos_y)

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.direction_x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction_x = 1
        else:
            self.direction_x = 0

        self.pos_x += self.direction_x * self.speed_x
        if self.pos_x <= 0:
            self.pos_x = 0
        elif self.pos_x >= src.lib.width - 100:
            self.pos_x = src.lib.width - 100

    def draw(self):
        self.game.screen.blit(self.irabbit, (self.pos_x, self.pos_y))


class stone:
    """
    The enemy
    """
    def __init__(self, game):
        self.game = game
        self.pos_x = randint(0, src.lib.width)
        self.pos_y = -50
        self.speed_y = 0
        self.acceleration_y = 9.8 / src.lib.FPS
        self.istone = pygame.image.load("src/stone.png")
        self.rect = self.istone.get_rect()
        self.rect.topleft = (self.pos_x, self.pos_y)

    def update(self):
        self.speed_y += self.acceleration_y
        self.pos_y += self.speed_y

    def draw(self):
        self.game.screen.blit(self.istone, (self.pos_x, self.pos_y))
