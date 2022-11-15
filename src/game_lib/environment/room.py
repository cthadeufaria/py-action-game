"""Class that stores state of a limited space inside the game environment."""
from typing import Tuple
from .map_grid import MapGrid


class Room:
    """Class that stores state of a limited space inside the game environment."""

    def __init__(
        self,
        room_id: str,
        dimensions: Tuple[int, int],
        map_image: str,
        map_grids: Tuple[Tuple[MapGrid]],
        soundtrack: str,
    ) -> None:
        """Initialize Room instance."""
        self.room_id = room_id
        self.dimensions = dimensions
        self.map_image = map_image  # convert to binary
        self.map_grids = map_grids
        self.soundtrack = soundtrack

        pass
