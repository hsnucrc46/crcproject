"""
4/14

DONE : 
1. click the start button to start the game
2. the player moves with the mouse
3. the stones fly from all sides
4. the speed of the stones can be changed
5. if a stone hits the player, the player's health decreases by 10%
6. if the player's health is 0%, the game will end
7. there is a timer : 30 seconds
8. if the timer stops and the player's health is more than 0% -> print("You WON")
9. the healthbar and timer is displayed on the screen

TO DO:
1. make the player stay in the middle of the screen
2. make the game full screen
3. make the shield to protect the player
4. make a function to shoot stones 
"""

import pygame
import random
import sys
import src.lib as lib
import src.sprites as sprites

quitgame = lib.quitgame

screen = pygame.display.set_mode((lib.width, lib.height))


# Load your background image here
background_img = pygame.transform.scale(pygame.image.load("background.jpg"), (lib.width, lib.height))



class game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(lib.caption)
        pygame.display.set_icon(pygame.image.load("icon.png"))
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

        if self.time <= 0:
            if PLAYER_HEALTH > 0:
                print("You WON!")
            quitgame()

    def draw(self):
        
        
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


# Create the start button

def start_game():

    # Create sprites group
    # https://gamedevacademy.org/pygame-sprite-group-tutorial-complete-guide/


    # Main loop
    while True:

        # Update countdown timer



        # Collisions with stones

        # Blit background image

        # Draw countdown timer
        # Convert frames back to seconds
        
        screen.blit(timer_text, (lib.width - 200, 10))

        if PLAYER_HEALTH <= 0:
            quitgame()

