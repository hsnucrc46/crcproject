"""
File: lib.py
Author: Oliver Tzeng, Crystal Diamond, 314Hello
Email: hsnucrc46@gmail.com
Github: https://github.com/hsnucrc46
Description: This file is a preference file, set your color, fps, player speed and more
"""

import pygame
from rich import print
import sys
from screeninfo import get_monitors

caption = "太空防衛戰"
color = "black"
fps = 60
max_health = 100
height = get_monitors()[0].height
width = get_monitors()[0].width
max = 2000
min = 250
max_time = 60
step = -10
time = 0


def quitgame(point=-1):
    if not point:
        print("[b magenta]你輸了[/b magenta]:skull:，最後得了 0 分")
    elif not point == -1:
        print("[b magenta]你輸了[/b magenta]，最後得了", point, "分")
        sys.exit()
    pygame.quit()
    quit()


def collision(sub, obj):
    """
    Check collision using rect attribute from your object.
    """
    height_obj = obj.rect.height
    height_sub = sub.rect.height
    width_obj = obj.rect.width
    width_sub = sub.rect.width
    pos_obj = obj.rect.topleft
    pos_sub = sub.rect.topleft

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
    screen,
    text,
    posX,
    posY,
    width,
    height,
    inActiveColor,
    activeColor,
    action=None,
):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    is_mouse_over = posX < mouse[0] < posX + width and posY < mouse[1] < posY + height

    button_color = activeColor if is_mouse_over else inActiveColor
    pygame.draw.rect(screen, button_color, (posX, posY, width, height))

    if is_mouse_over and click[0] == 1 and action is not None:
        action()
        return False

    draw_text(screen, text, 50, "black", posX + (width / 2), posY + (height / 2))
    return True


def draw_text(screen, text, size, color, x, y):
    font = pygame.font.SysFont("arial", size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)


def intro(clock, screen, action):
    """
    intro screen
    """
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
        screen.fill(color)
        draw_text(screen, "Level 2", 80, "white", width / 2, height / 2)
        if not button(
            screen,
            "Start",
            width * 3 / 5,
            height * 2 / 3,
            width / 5,
            height / 5,
            "white",
            "green",
            action=action.new,
        ):
            return 0
        button(
            screen,
            "Skip",
            width * 1 / 5,
            height * 2 / 3,
            width / 5,
            height / 5,
            "white",
            "red",
            action=quitgame,
        )
        pygame.display.update()
        clock.tick(fps)


def win(screen):
    print("you won!")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
        screen.fill("black")
        draw_text(screen, "You WIN!", 100, "white", width // 2, height // 2 - 100)
        button(
            screen,
            "Exit",
            width // 2 - 200,
            height // 3 * 2,
            400,
            160,
            "grey",
            (241, 250, 238),
            quitgame,
        )
        pygame.display.flip()


def timebar(screen, max_time):
    global time
    pygame.draw.rect(
        screen, "dark red", (width * 9 / 10, height / 5, width / 50, height * 2 / 5)
    )
    if time < max_time * fps:
        pygame.draw.rect(
            screen,
            "green",
            (
                width * 9 / 10,
                height / 5,
                width / 50,
                height * 2 / 5 * (max_time - time / fps) / max_time,
            ),
        )
    else:
        win(screen)
    draw_text(
        screen,
        str(max_time - int(time / fps)),
        50,
        "silver",
        width * 91 / 100,
        height / 5 - 50,
    )
    time = time + 1
