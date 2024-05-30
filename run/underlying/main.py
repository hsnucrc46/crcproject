"""
4/14

done :
    1. click the start button to start the game
2. the player moves with the mouse
3. the comets fly from all sides
4. the speed of the comets can be changed
5. if a comet hits the player, the player's health decreases by 10%
6. if the player's health is 0%, the game will end
7. there is a timer : 30 seconds
8. if the timer stops and the player's health is more than 0% -> print("you won")
9. the healthbar and timer is displayed on the screen
10. make the player stay in the middle of the screen
11. make the game full screen
12. modularize the sprites and the functions

TODO:
1. make the shield to protect the player
2. make a function to shoot comets
"""

import pygame
import src.lib as lib
import src.sprites as sprites
import sys

pygame.init()

quitgame = lib.quitgame


class game:
    def __init__(self):
        self.icon = pygame.image.load("underlying/src/icon.png")
        self.time_left = lib.max_time
        self.height = lib.height
        self.width = lib.width
        self.caption = lib.caption
        self.create_button = lib.create_button
        self.fps = lib.fps
        # fonts
        self.title_font = pygame.font.Font(None, 100)
        self.time_font = pygame.font.Font(None, 80)
        self.win_font = pygame.font.Font(None, 100)

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption(self.caption)

        self.ibackground = pygame.transform.scale(
            pygame.image.load("underlying/src/background.jpg"),
            (self.width, self.height),
        )

        self.title_text = self.title_font.render(self.caption, True, "white")
        self.title_rect = self.title_text.get_rect(
            center=(self.width // 2, self.height // 3)
        )
        self.clock = pygame.time.Clock()
        self.in_intro = True
        self.playing = True
        self.countdown_tick = self.time_left * 60  # reset countdown timer

        # create sprites group
        # https://gamedevacademy.org/pygame-sprite-group-tutorial-complete-guide/
        self.sprites_group = pygame.sprite.Group()
        self.comets = pygame.sprite.Group()

        self.player = sprites.player(game)
        self.sprites_group.add(self.player)
        self.draw_health_bar = lib.draw_health_bar

    def intro(self):
        pygame.display.set_icon(self.icon)
        while self.in_intro:
            self.events()
            self.screen.blit(self.ibackground, (0, 0))
            self.screen.blit(self.title_text, self.title_rect)
            self.create_button(
                self.screen,
                "Start",
                self.width // 2 - 200,
                self.height // 3 * 2,
                400,
                160,
                "grey",
                (241, 250, 238),
                self.run,
            )
            pygame.display.flip()

    def run(self):
        """
        what actually needs to be done after initializing the game
        """
        self.in_intro = False
        while self.playing:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(self.fps)
        self.win()

    def events(self):
        """
        know when to quit pygame
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

    def update(self):
        # update countdown timer
        self.countdown_tick -= 1
        if self.player.health > 0 and self.countdown_tick <= 0:
            self.playing = False

        if len(self.comets) < 5:
            self.comet = sprites.comet(game)
            self.sprites_group.add(self.comet)
            self.comets.add(self.comet)

        self.sprites_group.update()

        # collisions with self.comets
        hits = pygame.sprite.spritecollide(self.player, self.comets, True)
        for hit in hits:
            self.player.health -= 10
            hit.kill()

            if self.player.health <= 0:
                sys.exit()

    def draw(self):
        self.screen.blit(self.ibackground, (0, 0))  # blit background image
        if self.player.health <= 30:
            self.draw_health_bar(self.screen, 10, 10, self.player.health, "red")
        else:
            self.draw_health_bar(self.screen, 10, 10, self.player.health, "green")
        self.sprites_group.draw(self.screen)

        # draw countdown timer
        self.time_left = self.countdown_tick // 60  # convert frames back to seconds
        self.time_text = self.time_font.render(
            "Time Left: {} s".format(self.time_left), True, "white"
        )
        self.screen.blit(self.time_text, (self.width * 5 / 6, 10))
        pygame.display.flip()

    def win(self):
        print("you won!")
        win_text = self.win_font.render("You WIN!", True, "white")
        win_rect = win_text.get_rect(center=(self.width // 2, self.height // 2 - 100))
        while True:
            self.events()
            self.screen.blit(self.ibackground, (0, 0))
            self.screen.blit(win_text, win_rect)
            self.create_button(
                self.screen,
                "Skip",
                self.width // 2 - 200,
                self.height // 3 * 2,
                400,
                160,
                "grey",
                (241, 250, 238),
                quitgame,
            )
            pygame.display.flip()


game = game()
game.intro()
