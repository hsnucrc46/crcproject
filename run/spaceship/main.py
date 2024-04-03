"""
File: main.py
Author: Oliver
Email: hsnu.crc46th@gmail.com
Github: https://github.com/hsnucrc46
Description: Interacts sprites declared in src/sprites.py
"""

import sys
import pygame
from random import randint
from rich import print, table
from rich.markdown import Markdown
import src.sprites
import src.lib

with open("src/story.md") as readme:
    markdown = Markdown(readme.read())
print(markdown)

class Game:
    """
    the object Game runs the game buffer
    """

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((src.lib.width, src.lib.height))
        pygame.display.set_caption(src.lib.CAPTION)

        self.clock = pygame.time.Clock()
        self.point = 0
        self.playing = True
        self.last_spawn_stone = pygame.time.get_ticks()
        self.stones = []
        self.player = src.sprites.rabbit(self)

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

        if pygame.time.get_ticks() - self.last_spawn_stone >= randint(src.lib.min, src.lib.max):
            self.stones.append(src.sprites.stone(self))
            self.last_spawn_stone = pygame.time.get_ticks()

        for s in self.stones:
            s.update()
            if src.lib.collision(self.player, s):
                if not self.point:
                    print("[bold magenta]You lost :skull:[/bold magenta] with", self.point, "points in total")
                else:
                    print("[bold magenta]You lost[/bold magenta] with", self.point, "points in total")
                self.playing = False
                return
            if s.pos_y >= src.lib.height:
                self.stones.remove(s)
                self.point += 1

    def draw(self):
        """
        update to screen
        """
        self.screen.fill(src.lib.COLOR)
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
            self.clock.tick(src.lib.FPS)

game = Game()
game.run()
pygame.quit()
sys.exit()
