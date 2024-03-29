# Copyright (c) 2024 Oliver Tzeng. All Rights Reserved.
# created: 2024/03/06 13/38

from random import randint
import pygame
from src import lib, sprites


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((lib.width, lib.height))
        pygame.display.set_caption(lib.caption)

        self.clock = pygame.time.Clock()
        self.playing = True
        self.last_spawn_stone = pygame.time.get_ticks()
        self.stones = []
        self.player = sprites.rabbit(self)

    def events(self):
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    self.playing = False

    def update(self):

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
        self.screen.fill(lib.color)
        self.player.draw()
        for s in self.stones:
            s.draw()
        pygame.display.update()

    def run(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(lib.fps)


game = Game()
game.run()
pygame.quit()
quit()
