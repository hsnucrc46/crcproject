# Copyright (c) 2024 Oliver Tzeng. All Rights Reserved.
# created: 2024/03/06 13/38

from screeninfo import get_monitors

width = get_monitors()[0].width
height = get_monitors()[0].height
caption = "stone"
fps = 60
color = "white"


def compare(a, b, c):
    return a < b and b < c


def collision(self, obj_one, obj_two):
    """
    Check collision using rect attribute from your object.
    You can get rect using Surface.get_rect()
    """
    pos_one = obj_one.rect.topleft
    pos_two = obj_two.rect.topleft
    width_one = obj_one.rect.width
    height_one = obj_one.rect.height
    width_two = obj_two.rect.width
    height_two = obj_two.rect.height

    # 先判斷Y範圍有無重疊
    if (
        (pos_two[1] < pos_one[1] and pos_two[1] + height_two >= pos_one[1])
        or (
            pos_two[1] >= pos_one[1]
            and pos_two[1] + height_two <= pos_one[1] + height_one
        )
        or (
            pos_two[1] <= pos_one[1] + height_one
            and pos_two[1] + height_two > pos_one[1] + height_one
        )
    ):
        # 再判斷X範圍有無重疊
        if (
            (pos_two[0] < pos_one[0] and pos_two[0] + width_two >= pos_one[0])
            or (
                pos_two[0] >= pos_one[0]
                and pos_two[0] + width_two <= pos_one[0] + width_one
            )
            or (
                pos_two[0] <= pos_one[0] + width_one
                and pos_two[0] + width_two > pos_one[0] + width_one
            )
        ):
            return True

    return False
