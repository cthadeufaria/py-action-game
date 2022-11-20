"""Class that stores state of a limited space inside the game environment."""
import sys
from typing import Tuple
import pygame

try:
    sys.path.append("src")
    from utils.engine import load_png
except IndexError:
    exit()


class Room:
    """Class that stores state of a limited space inside the game environment."""

    def __init__(self, walls: list[pygame.Rect], map_image_path: str) -> None:
        """Initialize Room instance."""
        self.walls = walls
        self.map_surface, self.map_rect = load_png(map_image_path)

    def draw_map(
        self, screen: pygame.surface.Surface, pos_offset: Tuple[int, int]
    ) -> None:
        """Position room map depending on player's position."""
        screen.blit(
            self.map_surface,
            (
                self.map_rect.topleft[0] - pos_offset[0],
                self.map_rect.topleft[1] - pos_offset[1],
            ),
        )

    def position_walls(
        self, screen: pygame.surface.Surface, pos_offset: Tuple[int, int]
    ) -> None:
        """Position all walls depending on player's position."""
        for wall in self.walls:
            wall = wall.move(wall.topleft[0] - pos_offset[0], wall.topleft[1] - pos_offset[1])  # type: ignore
            # screen.blit image
            pygame.draw.rect(screen, "red", wall)  # TEMPORARY red for debugging purposes
