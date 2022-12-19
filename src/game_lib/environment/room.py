"""Class that stores state of a limited space inside the game environment."""
import json
from typing import Tuple
from ..elements.hero import Hero
from ..utils.engine import load_png, get_absolute_path
import pygame


class Room:
    """Class that stores state of a limited space inside the game environment."""

    def __init__(self, walls_file_path: str, map_image_path: str) -> None:
        """Initialize Room instance."""
        self.map_surface, self.map_rect = load_png(map_image_path)

        with open(
            get_absolute_path(__file__, "..", "constants", walls_file_path)
        ) as walls_file:
            walls_grid = json.load(walls_file)
            self.walls: list[pygame.Rect] = []

            for row_idx, row in enumerate(walls_grid):
                for col_idx, wall in enumerate(row):
                    if wall:
                        self.walls.append(
                            pygame.Rect(col_idx * 32, row_idx * 32, 32, 32)
                        )

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

    def position_walls(self, screen: pygame.surface.Surface, hero: Hero) -> None:
        """Position all walls depending on player's position."""
        for wall in self.walls:
            wall.move(
                -hero.rect.centerx + screen.get_size()[0] // 2,
                -hero.rect.centery + screen.get_size()[1] // 2,
            )

            # Draw wall for debugging purposes
            # pygame.draw.rect(
            #     screen, "red", wall
            # )
