"""
File: lib.py
Author: Oliver Tzeng, Crystal Diamond, 314Hello
Email: hsnucrc46@gmail.com
Github: https://github.com/hsnucrc46
Description: This file is a preference file, set your color, fps, player speed and more
"""

import sys

import pygame
from rich import print
from screeninfo import get_monitors

caption = "Level 1"
color = "black"
fps = 60
max_health = 100
height = get_monitors()[0].height
width = get_monitors()[0].width
max = 2000
min = 250
step = -10
max_time = 30
time = 0
directions = ["up", "down", "left", "right"]

# fonts
pygame.font.init()
button_font = pygame.font.Font(None, 80)


def quitgame():
    pygame.quit()
    quit()


def draw_health_bar(surface, x, y, health, color):
    bar_length = 1000
    bar_height = 50
    fill = (health / 100) * bar_length
    pygame.draw.rect(surface, color, (x, y, fill, bar_height))
    pygame.draw.rect(surface, "white", (x, y, bar_length, bar_height), 2)


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

    button_text = button_font.render(text, True, "black")
    text_rect = button_text.get_rect(center=(x + width / 2, y + height / 2))
    surface.blit(button_text, text_rect)
