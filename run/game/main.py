"""
file: main.py
author: 
email: hsnu.crc46th@gmail.com
github: https://github.com/hsnucrc46
description: interacts sprites declared in src/sprites.py
"""

import pygame
import src.lib

quitgame = src.lib.quitgame

class game:

    def __init__(self):
        pass

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.quit:
                quitgame()

    def update(self):
        pass

    def draw(self):
        self.screen.blit(self.ibackground, (0, 0))
        self.player.draw(self.screen)
        pygame.display.update()

    
    def run(self):
        self.events()
        self.update()
        self.draw()