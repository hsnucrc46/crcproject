"""
File: main.py
Author: Oliver
Email: hsnu.crc46th@gmail.com
Github: https://github.com/hsnucrc46
Description: Interacts sprites declared in src/sprites.py
"""

import sys
import pygame
import src.sprites
import src.lib

class Game:
    """
    the object Game runs the game buffer
    """

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((src.width, src.height))
        pygame.display.set_caption(src.CAPTION)

        self.clock = pygame.time.Clock()
        self.playing = True
        self.last_spawn_stone = pygame.time.get_ticks()
        self.stones = []
        self.player = src.rabbit(self)

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
            self.stones.append(src.stone(self))
            self.last_spawn_stone = pygame.time.get_ticks()

        for s in self.stones:
            s.update()
            if self.src.collision(self.player, s):
                print("You Lost")
                self.playing = False
            if s.pos_y >= src.height:
                self.stones.remove(s)

    def draw(self):
        """
        update to screen
        """
        self.screen.fill(src.COLOR)
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
            self.clock.tick(src.FPS)


game = Game()
game.run()
pygame.quit()
sys.exit()
