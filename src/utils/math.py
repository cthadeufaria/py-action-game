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


def check_inside_circle(
    point: Tuple[int, int], center: Tuple[int, int], radius: int
) -> bool:
    """Determine if a circle defined by its center and radius contains a point."""
    return ((point[0] - center[0]) ** 2 + (point[1] - center[1]) ** 2) <= (radius**2)
