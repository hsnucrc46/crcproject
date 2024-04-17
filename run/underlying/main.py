"""
file: main.py
author: 
email: hsnu.crc46th@gmail.com
github: https://github.com/hsnucrc46
description: interacts sprites declared in src/sprites.py
"""

import pygame
import src.lib as lib
import src.sprites as sprites

quitgame = lib.quitgame

screen = pygame.display.set_mode((lib.width, lib.height))


# Load your background image here
#background_img = pygame.transform.scale(pygame.image.load("background.jpg"), (lib.width, lib.height))



class game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(lib.caption)
        pygame.display.set_icon(pygame.image.load("src/icon.png"))
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((lib.width, lib.height))
        self.fps = lib.fps

    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.stones = pygame.sprite.Group()
        self.player = sprites.Player(self)
        self.all_sprites.add(self.player)
        self.step = lib.health_step
        self.healthbar = self.player.draw_health_bar
        self.max_time = lib.max_time
        self.time = 0
        self.timer_text = lib.BUTTON_FONT.render("Time left: {}s".format((self.max_time-self.time)//self.fps), True, "white")

        self.run()
    
    def events(self):
        """
        know when to quit pygame
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

    def update(self):
        self.all_sprites.update()
        
        if len(self.stones) < 5:
            stone = sprites.Stone()
            self.all_sprites.add(stone)
            self.stones.add(stone)
        
        hits = pygame.sprite.spritecollide(self.player, self.stones, True)
        for hit in hits:
            PLAYER_HEALTH -= 10
            hit.kill()

        self.time +=1
        screen.blit(self.timer_text, (lib.width - 200, 10))
        if self.time == self.max_time:
            if PLAYER_HEALTH > 0:
                print("You WON!")
            quitgame()

        if self.player.health == 0:
            quitgame()

    def draw(self):
        
        self.screen.fill("black")
        self.screen.blit(pygame.image.load("src/background.jpg"), (0, 0))
        self.healthbar()
        self.all_sprites.draw(screen)
        pygame.display.update()
    
    def run(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(self.fps)


game = game()
lib.intro(game.clock, game.screen, game)