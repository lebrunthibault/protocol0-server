import math
from typing import Tuple

import pyautogui
from PIL import ImageGrab
from loguru import logger

from api.settings import Settings
from lib.enum.InterfaceColorEnum import InterfaceColorEnum


def move_to(x: int, y: int) -> None:
    pyautogui.moveTo(x, y)


def drag_to(x: int, y: int, duration=0.5) -> None:
    # pyautogui.mouseDown(button='left')
    # pyautogui.moveTo(x, y, button='left')
    # sleep(2)
    # pyautogui.mouseUp(button='left')
    pyautogui.dragTo(x, y, button='left', duration=duration, tween=pyautogui.easeOutQuad)


def click(x: int, y: int, keep_position=True, exact=False) -> None:
    # coordinates are relative to a 1080p display resolution
    # accounting for resolution change
    if not exact:
        x *= Settings().display_resolution_factor
        y *= Settings().display_resolution_factor

    mouse_position = pyautogui.position()

    try:
        pyautogui.click(x, y)
    except pyautogui.FailSafeException as e:
        logger.warning(e)

    if keep_position:
        pyautogui.moveTo(mouse_position)


def click_vertical_zone(x: int, y: int) -> None:
    for i in range(120, -40, -20):
        pyautogui.click(x, y + i)


def get_pixel_color_at(x: int, y: int) -> Tuple[int, int, int]:
    image = ImageGrab.grab()
    pixel_color = image.getpixel((x, y))
    logger.debug("pixel_color: %s" % InterfaceColorEnum.get_string_from_tuple(pixel_color))
    return pixel_color


def color_distance(c1, c2):
    # type: (Tuple[int, int, int], Tuple[int, int, int]) -> float
    (r1, g1, b1) = c1
    (r2, g2, b2) = c2
    return math.sqrt((r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2)
