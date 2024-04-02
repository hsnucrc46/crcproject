"""
File: main.py
Author: Oliver
Email: hsnu.crc46th@gmail.com
Github: https://github.com/hsnucrc46
Description: Interacts sprites declared in src/sprites.py
"""

import sys
import pygame
from src import sprites, lib


class Game:
    """
    the object Game runs the game buffer
    """

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((lib.width, lib.height))
        pygame.display.set_caption(lib.CAPTION)

        self.clock = pygame.time.Clock()
        self.playing = True
        self.last_spawn_stone = pygame.time.get_ticks()
        self.stones = []
        self.player = sprites.rabbit(self)

    def events(self):
        """
        know when to quit pygame
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        """
        detect user input
        """
        self.player.update(pygame.key.get_pressed())

        if pygame.time.get_ticks() - self.last_spawn_stone >= 1000:
            self.stones.append(sprites.stone(self))
            self.last_spawn_stone = pygame.time.get_ticks()

        for s in self.stones:
            s.update()
            if self.lib.collision(self.player, s):
                print("You Lost")
                self.playing = False
            if s.pos_y >= lib.height:
                self.stones.remove(s)

    def draw(self):
        """
        update to screen
        """
        self.screen.fill(lib.COLOR)
        self.player.draw()
        for s in self.stones:
            s.draw()
        pygame.display.update()

    def run(self):
        """
        what actually needs to be done after initializing the game
        """
        while self.playing:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(lib.FPS)


game = Game()
game.run()
pygame.quit()
sys.exit()
