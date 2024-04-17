"""
File: lib.py
Author: Oliver Tzeng, Crystal Diamond, 314Hello
Email: hsnucrc46@gmail.com
Github: https://github.com/hsnucrc46
Description: This file is a preference file, set your color, fps, player speed and more
"""

import pygame
from rich import print
from screeninfo import get_monitors

caption = "comet defense game"
color = "black"
fps = 60
max_health = 100
height = get_monitors()[0].height
width = get_monitors()[0].width
max = 2000
min = 250
max_time = 30
step = -10
time = 0
direction = "up"


def quitgame(point=-1):
    if not point:
        print("[b magenta]你輸了[/b magenta]:skull:，最後得了 0 分")
    elif not point == -1:
        print("[b magenta]你輸了[/b magenta]，最後得了", point, "分")
    pygame.quit()
    quit()


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
