"""Auxiliary mathematical functions."""
from typing import Tuple


def get_center_coordinates(
    screen_size: Tuple[int, int], width: int, height: int
) -> Tuple[int, int]:
    """Return x, y position to center a rect.

    Gets the size of the screen and the dimensions of a rectangle and
    gives the coordinates for the top left corner that allow the
    rectangle to be at the center of the screen.

    """
    return (screen_size[0] - width) // 2, (screen_size[1] - height) // 2
