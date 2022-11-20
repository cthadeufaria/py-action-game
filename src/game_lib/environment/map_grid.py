"""Class that stores state and visual information about a unit square inside a room."""
from typing import Tuple


class MapGrid:
    """Class that stores state and visual information about a unit square inside a room."""

    def __init__(
        self, position: Tuple[int, int], image: str, walkable: bool, leading_room: str
    ) -> None:
        """Initialize MapGrid instance."""
        self.position = position
        self.image = image  # convert to binary
        self.walkable = walkable
        self.leading_room = leading_room
