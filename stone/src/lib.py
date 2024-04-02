# Copyright (c) 2024 HSNU CRC. All Rights Reserved.
# created: 2024/03/06 13/38

from screeninfo import get_monitors

width = get_monitors()[0].width
height = get_monitors()[0].height
CAPTION = "stone"
FPS = 60
COLOR = "white"


def collision(self, sub, obj):
    """
    Check collision using rect attribute from your object.
    You can get rect using Surface.get_rect()
    """
    pos_sub = sub.rect.topleft
    pos_obj = obj.rect.topleft
    width_sub = sub.rect.width
    height_sub = sub.rect.height
    width_obj = obj.rect.width
    height_obj = obj.rect.height

    # Check if objects are colliding along the y-axis
    y_colliding = (
        pos_obj[1] < pos_sub[1] + height_sub and pos_obj[1] + height_obj >= pos_sub[1]
    )

    # Check if objects are colliding along the x-axis
    x_colliding = (
        pos_obj[0] < pos_sub[0] + width_sub and pos_obj[0] + width_obj >= pos_sub[0]
    )

    # Check if objects are colliding in both x and y directions
    return y_colliding and x_colliding
