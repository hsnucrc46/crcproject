"""
File: main.py
Author: Oliver Tzeng, Crystal Diamond, 314hello
Email: hsnu.crc46th@gmail.com
Github: https://github.com/hsnucrc46
Description: Interacts sprites declared in src/sprites.py
"""

import pygame
import functools
from random import randint
from rich import print
import src.sprites
import src.lib


class Game:
    """
    the object Game runs the game buffer
    """

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((src.lib.width, src.lib.height))
        pygame.display.set_caption(src.lib.CAPTION)
        self.clock = pygame.time.Clock()
        src.lib.intro = False
        self.point = 0
        self.last_spawn_comet = pygame.time.get_ticks()
        self.comets = []
        self.player = src.sprites.spaceship(self)

    def events(self):
        """
        know when to quit pygame
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                src.lib.quitgame()

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
                self.player.health -= 10
                self.comets.remove(s)
                if not self.point:
                    print(
                        "[b magenta]你輸了[/b magenta]:skull:，最後得了",
                        self.point,
                        "分",
                    )
                else:
                    print("[b magenta]你輸了[/b magenta]，最後得了", self.point, "分")
                src.lib.quitgame()
            if s.pos_y >= src.lib.height:
                self.comets.remove(s)
                self.point += 1
        
        if (self.player.health==0):
            if not self.point:
                    print(
                        "[b magenta]你輸了[/b magenta]:skull:，最後得了",
                        self.point,
                        "分",
                    )
            else:
                print("[b magenta]你輸了[/b magenta]，最後得了", self.point, "分")
            src.lib.quitgame()

    def draw(self):
        """
        update to screen
        """
        self.screen.fill(src.lib.COLOR)
        self.player.draw()
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
        src.lib.time_bar(self.screen, self.clock.get_time())
        self.clock.tick(src.lib.FPS)


def bind_method(method, *args, **kwargs):
    return lambda: method(*args, **kwargs)


game = Game()
bound_run = functools.partial(bind_method, game.run)
src.lib.intro(game.clock, game.screen, bound_run)
game.run()
