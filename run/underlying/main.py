"""
4/14

done :
1. click the start button to start the game
2. the player moves with the mouse
3. the stones fly from all sides
4. the speed of the stones can be changed
5. if a stone hits the player, the player's health decreases by 10%
6. if the player's health is 0%, the game will end
7. there is a timer : 30 seconds
8. if the timer stops and the player's health is more than 0% -> print("you won")
9. the healthbar and timer is displayed on the screen

todo:
1. make the player stay in the middle of the screen
2. make the game full screen
3. make the shield to protect the player
4. make a function to shoot stones
"""

import random
import sys

import pygame
import src.lib as lib

pygame.init()

height = lib.height
width = lib.width
lib.height = 600
player_size = 50
stone_size = 30
stone_speed = 10
player_health = 100
countdown_seconds = 30

# fonts
button_font = pygame.font.font(none, 40)
title_font = pygame.font.font(none, 60)

screen = pygame.display.set_mode((lib.width, lib.height))
pygame.display.set_caption("stone defense game")

background_img = pygame.image.load("background.jpg")  # load your background image here
background_img = pygame.transform.scale(background_img, (lib.width, lib.height))
player_img = pygame.image.load("player.png")
player_img = pygame.transform.scale(player_img, (player_size, player_size))
stone_img = pygame.image.load("stone.png")
stone_img = pygame.transform.scale(stone_img, (stone_size, stone_size))
icon_img = pygame.image.load("icon.png")
pygame.display.set_icon(icon_img)

clock = pygame.time.clock()


class player(pygame.sprite.sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect(center=(lib.width // 2, lib.height // 2))

    def update(self):
        self.rect.center = pygame.mouse.get_pos()


class stone(pygame.sprite.sprite):
    def __init__(self):
        super().__init__()
        self.image = stone_img
        self.rect = self.image.get_rect()
        self.direction = random.choice(["right", "left", "up", "down"])
        if self.direction == "right":
            self.rect.x = 0 - stone_size
            self.rect.y = random.randint(0, lib.height - stone_size)
            self.speed_x = stone_speed
            self.speed_y = 0
        elif self.direction == "left":
            self.rect.x = lib.width
            self.rect.y = random.randint(0, lib.height - stone_size)
            self.speed_x = -stone_speed
            self.speed_y = 0
        elif self.direction == "up":
            self.rect.x = random.randint(0, lib.width - stone_size)
            self.rect.y = lib.height
            self.speed_x = 0
            self.speed_y = -stone_speed
        elif self.direction == "down":
            self.rect.x = random.randint(0, lib.width - stone_size)
            self.rect.y = 0 - stone_size
            self.speed_x = 0
            self.speed_y = stone_speed

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if (
            self.rect.right < 0
            or self.rect.left > lib.width
            or self.rect.bottom < 0
            or self.rect.top > lib.height
        ):
            self.kill()


def draw_health_bar(surface, x, y, health):
    bar_length = 100
    bar_height = 10
    fill = (health / 100) * bar_length
    outline_rect = pygame.rect(x, y, bar_length, bar_height)
    fill_rect = pygame.rect(x, y, fill, bar_height)
    pygame.draw.rect(surface, red, fill_rect)
    pygame.draw.rect(surface, white, outline_rect, 2)


# create the start button
def create_button(
    surface, text, x, y, width, height, inactive_color, active_color, action
):
    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x < mouse_pos[0] < x + width and y < mouse_pos[1] < y + height:
        pygame.draw.rect(surface, active_color, (x, y, width, height))
        if click[0] == 1:
            action()
    else:
        pygame.draw.rect(surface, inactive_color, (x, y, width, height))

    button_text = button_font.render(text, true, black)
    text_rect = button_text.get_rect(center=(x + width / 2, y + height / 2))
    surface.blit(button_text, text_rect)


def start_game():
    global countdown_timer, player_health
    countdown_timer = countdown_seconds * 60  # reset countdown timer
    player_health = 100  # reset player health

    # create sprites group
    # https://gamedevacademy.org/pygame-sprite-group-tutorial-complete-guide/
    all_sprites = pygame.sprite.group()
    stones = pygame.sprite.group()

    player = player()
    all_sprites.add(player)

    # main loop
    while true:
        for event in pygame.event.get():
            if event.type == pygame.quit:
                pygame.quit()
                sys.exit()

        # update countdown timer
        countdown_timer -= 1
        if countdown_timer <= 0:
            if player_health > 0:
                print("you won!")
            pygame.quit()
            sys.exit()

        if len(stones) < 5:
            stone = stone()
            all_sprites.add(stone)
            stones.add(stone)

        all_sprites.update()

        # collisions with stones
        hits = pygame.sprite.spritecollide(player, stones, true)
        for hit in hits:
            player_health -= 10

        screen.blit(background_img, (0, 0))  # blit background image
        all_sprites.draw(screen)
        draw_health_bar(screen, 10, 10, player_health)

        # draw countdown timer
        countdown_seconds = countdown_timer // 60  # convert frames back to seconds
        timer_text = button_font.render(
            "time left: {}s".format(countdown_seconds), true, white
        )
        screen.blit(timer_text, (lib.width - 200, 10))

        if player_health <= 0:
            pygame.quit()
            sys.exit()

        pygame.display.flip()
        clock.tick(60)


def main():
    while true:
        for event in pygame.event.get():
            if event.type == pygame.quit:
                pygame.quit()
                sys.exit()

        screen.fill(black)

        screen.blit(background_img, (0, 0))

        title_text = title_font.render("stone defense game", true, white)
        title_rect = title_text.get_rect(center=(lib.width // 2, lib.height // 3))
        screen.blit(title_text, title_rect)

        # start button
        create_button(screen, "start", 300, 350, 200, 80, gray, light, start_game)

        pygame.display.flip()
        clock.tick(60)


main()
