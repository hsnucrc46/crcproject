"""
File: lib.py
Author: Oliver Tzeng
Email: hsnucrc46@gmail.com
Github: https://github.com/hsnucrc46
Description: This file is a preference file, set your color, fps, player speed and more
"""

from screeninfo import get_monitors
import sys
import pygame

width = get_monitors()[0].width
height = get_monitors()[0].height
min = 250
max = 2000
CAPTION = "太空防衛戰"
FPS = 60
COLOR = "black"


def collision(sub, obj):
    """
    Check collision using rect attribute from your object.
    """
    pos_sub = sub.rect.topleft
    pos_obj = obj.rect.topleft
    width_sub = sub.rect.width
    height_sub = sub.rect.height
    width_obj = obj.rect.width
    height_obj = obj.rect.height

    """
    Check if objects are colliding along the y-axis
    """
    y_colliding = (
        pos_obj[1] < pos_sub[1] + height_sub and pos_obj[1] + height_obj >= pos_sub[1]
    )

    """
    Check if objects are colliding along the y-axis
    """
    x_colliding = (
        pos_obj[0] < pos_sub[0] + width_sub and pos_obj[0] + width_obj >= pos_sub[0]
    )

    return y_colliding and x_colliding


def button(
    screen, text, posX, posY, width, height, inActiveColor, activeColor, action=None
):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    is_mouse_over = posX < mouse[0] < posX + width and posY < mouse[1] < posY + height

    button_color = activeColor if is_mouse_over else inActiveColor
    pygame.draw.rect(screen, button_color, (posX, posY, width, height))

    if is_mouse_over and click[0] == 1 and action is not None:
        action()

    draw_text(screen, text, 50, "black", posX + (width / 2), posY + (height / 2))


def draw_text(screen, text, size, color, x, y):
    font = pygame.font.SysFont("arial", size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)


def intro(clock, screen, action):
    """
    startscreen
    """
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
        screen.fill(COLOR)
        draw_text(screen, "Level 2", 80, "white", width / 2, height / 2)
        button(
            screen,
            "Begin",
            width * 3 / 5,
            height * 2 / 3,
            width / 5,
            height / 5,
            "white",
            "green",
            action(),
        )
        button(
            screen,
            "Exit",
            width * 1 / 5,
            height * 2 / 3,
            width / 5,
            height / 5,
            "white",
            "red",
            action=quitgame,
        )
        pygame.display.update()
        clock.tick(FPS)


def quitgame():
    intro = False
    pygame.quit()
    sys.exit()
