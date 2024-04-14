"""
file: main.py
author: Oliver Tzeng, Crystal Diamond, 314hello
email: hsnu.crc46th@gmail.com
github: https://github.com/hsnucrc46
description: interacts sprites declared in src/sprites.py
"""

from random import randint

import pygame
import src.lib as lib
import src.sprites as sprites

quitgame = lib.quitgame


class game:
    """
    the object game runs the game buffer
    """

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(lib.caption)
        self.clock = pygame.time.Clock()
        self.fps = lib.fps
        self.height = lib.height
        self.playing = True
        self.point = 0
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.step = lib.step
        self.timebar = lib.timebar

    def new(self):
        self.player = sprites.spaceship(self)
        self.collision = lib.collision
        self.comets = []
        self.comet_pool = sprites.CometPool(self)
        self.healthbar = self.player.healthbar
        self.last_spawn_comet = pygame.time.get_ticks()
        self.max = lib.max
        self.max_time = lib.max_time
        self.min = lib.min
        self.run()

    def events(self):
        """
        know when to quit pygame
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame(self.point)

    def update(self):
        """
        detect user input
        """
        self.player.update(pygame.key.get_pressed())

        self.now = pygame.time.get_ticks()
        if self.now - self.last_spawn_comet >= randint(self.min, self.max):
            self.comet_pool.create_comet()
            self.last_spawn_comet = self.now

        self.comet_pool.update()  # Update all comets in the CometPool

        # Check for collisions with player and handle removal of comets
        for s in self.comet_pool:
            if self.collision(self.player, s):
                self.player.health += self.step
                self.comet_pool.comets.remove(s)
            elif s.pos_y >= self.height:
                self.comet_pool.comets.remove(s)
                self.point += 1

        if not self.player.health:
            quitgame(self.point)

    def draw(self):
        """
        update to screen
        """
        self.screen.fill("black")
        self.player.draw(self.screen)
        self.healthbar(self.screen)
        self.timebar(self.screen, self.max_time, quitgame)
        self.comet_pool.draw()
        pygame.display.update()

    def run(self):
        """
        what actually needs to be done after initializing the game
        """
        while self.playing:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(self.fps)


game = game()
lib.intro(game.clock, game.screen, game)
quitgame(self.point)
