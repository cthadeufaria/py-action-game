"""Class that stores state of a limited space inside the game environment."""
from typing import Tuple
from .map_grid import MapGrid
import pygame


class Room:
    """Class that stores state of a limited space inside the game environment."""

    def __init__(self, walls: list[pygame.Rect]) -> None:
        """Initialize Room instance."""
        self.walls = walls

    def position_walls(
        self, screen: pygame.surface.Surface, pos_offset: Tuple[int, int]
    ) -> None:
        """Position all walls depending on player's position."""
        for wall in self.walls:
            wall = wall.move(wall.topleft[0] - pos_offset[0], wall.topleft[1] - pos_offset[1])  # type: ignore
            # screen.blit image
            pygame.draw.rect(screen, "red", wall)
