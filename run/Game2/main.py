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
        screen = pygame.display.set_mode((lib.width, lib.height))

    def new(self):
        all_sprites = pygame.sprite.Group()
        stones = pygame.sprite.Group()
        self.player = sprites.Player(self)
        all_sprites.add(self.player)
    
    def events(self):
        """
        know when to quit pygame
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

    def update(self):
        pass


# Create the start button

def start_game():

    # Create sprites group
    # https://gamedevacademy.org/pygame-sprite-group-tutorial-complete-guide/


    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update countdown timer
        countdown_timer -= 1
        if countdown_timer <= 0:
            if PLAYER_HEALTH > 0:
                print("You WON!")
            pygame.quit()
            sys.exit()

        if len(stones) < 5:
            stone = sprites.Stone()
            all_sprites.add(stone)
            stones.add(stone)

        all_sprites.update()

        # Collisions with stones
        hits = pygame.sprite.spritecollide(player, stones, True)
        for hit in hits:
            PLAYER_HEALTH -= 10

        screen.blit(background_img, (0, 0))  # Blit background image
        all_sprites.draw(screen)
        draw_health_bar(screen, 10, 10, PLAYER_HEALTH)

        # Draw countdown timer
        lib.time = countdown_timer // lib.fps  # Convert frames back to seconds
        timer_text = lib.BUTTON_FONT.render("Time left: {}s".format(countdown_seconds), True, "white")
        screen.blit(timer_text, (lib.width - 200, 10))

        if PLAYER_HEALTH <= 0:
            quitgame()

        pygame.display.update()
        self.clock.tick(lib.fps)

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill("black")

        screen.blit(background_img, (0, 0))

        title_text = lib.TITLE_FONT.render(lib.caption, True, "white")
        title_rect = title_text.get_rect(center=(lib.width // 2, lib.height // 3))
        screen.blit(title_text, title_rect)

        # Start button
        lib.create_button(screen, "Start", 300, 350, 200, 80, "grey", "honeydew1", start_game)

        pygame.display.flip()
        clock.tick(lib.fps)

main()
