# Copyright (c) 2024 Oliver Tzeng. All Rights Reserved.
# created: 2024/03/06 13/38

import sys, pygame
import src.sprites, src.lib


# the object Game runes the game buffer
class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((src.lib.width, src.lib.height))
        pygame.display.set_caption(src.lib.caption)

        self.clock = pygame.time.Clock()
        self.playing = True
        self.last_spawn_stone = pygame.time.get_ticks()
        self.stones = []
        self.player = src.sprites.rabbit(self)

    # know when to quit pygame
    def events(self):
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    self.playing = False

    # detect user input
    def update(self):

        self.player.update(pygame.key.get_pressed())

        if pygame.time.get_ticks() - self.last_spawn_stone >= 1000:
            self.stones.append(src.sprites.stone(self))
            self.last_spawn_stone = pygame.time.get_ticks()

        for s in self.stones:
            s.update()
            if self.src.lib.collision(self.player, s):
                print("You Lost")
                self.playing = False
            if s.pos_y >= src.lib.height:
                self.stones.remove(s)

    # update to screen
    def draw(self):
        self.screen.fill(src.lib.color)
        self.player.draw()
        for s in self.stones:
            s.draw()
        pygame.display.update()

    def run(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(src.lib.fps)


game = Game()
game.run()
pygame.quit()
sys.exit()
