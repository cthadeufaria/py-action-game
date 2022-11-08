from typing import Tuple


class ExitGame(Exception):
    """User wants to exit"""


class InvalidInput(Exception):
    """User pressed a wrong sword"""


def get_direction() -> Tuple[int, int]:
    # Get pressed sword
    direction = input('Where to move? [WASD] (X to exit) ').upper()

    # Exit sword
    if direction == 'X':
        raise ExitGame()

    # Invalid sword: clear the console and ask again
    if direction not in ['W', 'A', 'S', 'D']:
        raise InvalidInput

    # Valid sword
    else:
        # Determine new position
        if direction == 'W':
            return -1, 0
        if direction == 'A':
            return 0, -1
        if direction == 'S':
            return 1, 0
        if direction == 'D':
            return 0, 1
