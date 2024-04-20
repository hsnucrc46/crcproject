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


class Spaceship:
    """
    The player
    """

    def __init__(self, game):
        self.game = game
        self.health = lib.max_health
        self.ispaceship = pygame.transform.rotozoom(
            pygame.image.load("spaceship/src/spaceship.png"), 0, 0.1
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
        pygame.draw.rect(
            screen, (0, 255, 0), (50, 50, self.health / lib.max_health * 200, 50)
        )

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
        elif self.pos_x >= self.width - self.rect.width:
            self.pos_x = self.width - self.rect.width
        self.rect.topleft = (self.pos_x, self.pos_y)

    def draw(self):
        self.game.screen.blit(self.ispaceship, (self.pos_x, self.pos_y))


class CometPool:
    def __init__(self, game):
        self.game = game
        self.comets = []

    def create_comet(self):
        new_comet = comet(self.game)
        self.comets.append(new_comet)

    def update(self):
        for comet in self.comets:
            comet.update()

    def draw(self):
        for comet in self.comets:
            comet.draw()

        # Optionally, you can add logic here to remove off-screen comets from the pool
        self.comets = [comet for comet in self.comets if comet.rect.top < lib.height]

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        if self.current < len(self.comets):
            comet = self.comets[self.current]
            self.current += 1
            return comet
        else:
            raise StopIteration


class comet:
    """
    The enemy
    """

    def __init__(self, game):
        self.game = game
        self.icomet = pygame.transform.rotozoom(
            pygame.image.load("spaceship/src/comet.png"), 0, 0.1
        )
        self.rect = self.icomet.get_rect()
        self.pos_x = randint(0, lib.width - self.rect.width)
        self.pos_y = 0 - self.rect.height
        self.speed_y = 0
        self.acceleration_y = 9.8 / lib.fps
        self.rect.topleft = (self.pos_x, self.pos_y)

    def update(self):
        self.speed_y += self.acceleration_y
        self.pos_y += self.speed_y
        self.rect.topleft = (self.pos_x, self.pos_y)

    def draw(self):
        self.game.screen.blit(self.icomet, (self.pos_x, self.pos_y))
