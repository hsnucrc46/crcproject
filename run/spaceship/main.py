"""
file: main.py
author: Oliver Tzeng, Crystal Diamond, 314hello
email: hsnu.crc46th@gmail.com
github: https://github.com/hsnucrc46
description: interacts sprites declared in src/sprites.py
"""

from random import randint

import pygame
import src.lib
import src.sprites

quitgame = src.lib.quitgame


class game:
    """
    the object game runs the game buffer
    """

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(src.lib.caption)
        self.clock = pygame.time.Clock()
        self.collision = src.lib.collision
        self.ibackground = pygame.image.load("src/bg.png")
        self.comets = []
        self.height = src.lib.height
        self.last_spawn_comet = pygame.time.get_ticks()
        self.max = src.lib.max
        self.max_time = src.lib.max_time
        self.min = src.lib.min
        self.player = src.sprites.spaceship(self)
        self.point = 0
        self.screen = pygame.display.set_mode((src.lib.width, self.height))
        self.step = src.lib.step
        self.health_bar = src.lib.health_bar
        self.time_bar = src.lib.time_bar

    def events(self):
        """
        know when to quit pygame
        """
        for event in pygame.event.get():
            if event.type == pygame.quit:
                quitgame(self.point)

    def update(self):
        """
        detect user input
        """
        self.player.update(pygame.key.get_pressed())

        if pygame.time.get_ticks() - self.last_spawn_comet >= randint(
            self.min, self.max
        ):
            self.comets.append(src.sprites.comet(self))
            self.last_spawn_comet = pygame.time.get_ticks()

        for s in self.comets:
            s.update()
            if self.collision(self.player, s):
                self.player.health += self.step
                self.comets.remove(s)
            elif s.pos_y >= self.height:
                self.comets.remove(s)
                self.point += 1

        if self.player.health == 0:
            quitgame(self.point)

    def draw(self):
        """
        update to screen
        """
        self.screen.blit(self.ibackground, (0, 0))
        self.player.draw(self.screen)
        self.health_bar(self.player, self.screen)
        self.time_bar(self.screen, self.max_time, quit)
        for s in self.comets:
            s.draw()
        pygame.display.update()

    def run(self):
        """
        what actually needs to be done after initializing the game
        """
        self.events()
        self.update()
        self.draw()
        self.clock.tick(src.lib.fps)


game = game()
src.lib.intro(game.clock, game.screen, game, bintro=True)
quitgame(game.point)
