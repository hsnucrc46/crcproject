"""
file: main.py
author: oliver tzeng, crystal diamond, 314hello
email: hsnu.crc46th@gmail.com
github: https://github.com/hsnucrc46
description: interacts sprites declared in src/sprites.py
"""

from random import randint

import pygame
import src.lib
import src.sprites


class game:
    """
    the object game runs the game buffer
    """

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(src.lib.caption)
        self.clock = pygame.time.clock()
        self.comets = []
        self.last_spawn_comet = pygame.time.get_ticks()
        self.player = src.sprites.spaceship(self)
        self.point = 0
        self.screen = pygame.display.set_mode((src.lib.width, src.lib.height))

    def events(self):
        """
        know when to quit pygame
        """
        for event in pygame.event.get():
            if event.type == pygame.quit:
                src.lib.quitgame(self.point)

    def update(self):
        """
        detect user input
        """
        self.player.update(pygame.key.get_pressed())

        if pygame.time.get_ticks() - self.last_spawn_comet >= randint(
            src.lib.min, src.lib.max
        ):
            self.comets.append(src.sprites.comet(self))
            self.last_spawn_comet = pygame.time.get_ticks()

        for s in self.comets:
            s.update()
            if src.lib.collision(self.player, s):
                self.player.health += src.lib.step
                self.comets.remove(s)
            elif s.pos_y >= src.lib.height:
                self.comets.remove(s)
                self.point += 1

        if self.player.health == 0:
            src.lib.quitgame(self.point)

    def draw(self):
        """
        update to screen
        """
        self.screen.fill(src.lib.color)
        self.player.draw(self.screen)
        for s in self.comets:
            s.draw()
        pygame.display.update()

    def run(self):
        """
        what actually needs to be done after initializing the game
        """
        pygame.display.update()
        self.events()
        self.update()
        self.draw()
        src.lib.time_bar(self.screen, self.clock, src.lib.max_time, quit)


game = game()
src.lib.intro(game.clock, game.screen, game, bintro=true)
src.lib.quitgame(game.point)
