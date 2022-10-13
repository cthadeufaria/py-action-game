from typing import Tuple


class ExitGame(Exception):
    """User wants to exit"""


class InvalidInput(Exception):
    """User pressed a wrong key"""


def get_direction() -> Tuple[int, int]:
    # Get pressed key
    direction = input('Where to move? [WASD] (X to exit) ').upper()

    # Exit key
    if direction == 'X':
        raise ExitGame()

    # Invalid key: clear the console and ask again
    if direction not in ['W', 'A', 'S', 'D']:
        raise InvalidInput

    # Valid key
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
