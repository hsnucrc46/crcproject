"""
File: lib.py
Author:
Email: hsnucrc46@gmail.com
Github: https://github.com/hsnucrc46
Description: This file is a preference file, set your color, fps, player speed and more
"""


import pygame

caption = "Stone Defense Game"

width = 800
height = 600
player_size = 50
stone_size = 30
stone_speed = 10
player_health = 100
health_step = -10
max_time = 30
time = 0
fps = 60


# Fonts
pygame.font.init()
BUTTON_FONT = pygame.font.Font(None, 40)
TITLE_FONT = pygame.font.Font(None, 60)


def quitgame():
    pygame.quit()
    quit()


def create_button(surface, text, x, y, width, height, inactive_color, active_color, action):
    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x < mouse_pos[0] < x + width and y < mouse_pos[1] < y + height:
        pygame.draw.rect(surface, active_color, (x, y, width, height))
        if click[0] == 1:
            action()
    else:
        pygame.draw.rect(surface, inactive_color, (x, y, width, height))

    button_text = BUTTON_FONT.render(text, True, "black")
    text_rect = button_text.get_rect(center=(x + width / 2, y + height / 2))
    surface.blit(button_text, text_rect)


def intro(clock, screen, action):

    while True:
        screen.fill("black")
        title_text = TITLE_FONT.render(caption, True, "white")
        title_rect = title_text.get_rect(center=(width // 2, height // 3))
        screen.blit(title_text, title_rect)
        create_button(
            screen, "start", 1, 1, 1, 1, "grey", "honeydew2", action)
        )
        clock.tick(fps)