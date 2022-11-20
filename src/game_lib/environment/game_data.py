"""Class that stores state of the game environment."""
from typing import Tuple
import pygame
from .room import Room
from ..elements.hero import Hero
from random import choice


class GameData:
    """Class that stores state of the game environment."""

    def __init__(
        self,
        screen: pygame.surface.Surface,
        clock: pygame.time.Clock,
        fps: int,
        bg_color: Tuple[int, int, int],
    ) -> None:
        """Initialize GameData instance."""

        self.screen = screen
        self.clock = clock
        self.fps = fps
        self.bg_color = bg_color

        # Get screen dimensions
        w, h = pygame.display.get_surface().get_size()
        self.temp_tile_size = 10

        # Generate temp map
        self.temp_map: list[list[str]] = [
            ["x" for _ in range(w // self.temp_tile_size)],
            *[
                [
                    "x",
                    *[choice([" ", "x"]) for _ in range(-2 + w // self.temp_tile_size)],
                    "x",
                ]
                for _ in range(-2 + h // self.temp_tile_size)
            ],
            ["x" for _ in range(w // self.temp_tile_size)],
        ]

    def game_loop(self) -> None:
        """Run each iteration of the game at a constant frame rate."""
        hero = Hero(
            position=(600, 300),
            image_paths=["bat.png"],
            dimensions=(50, 50),
            base_speed=2,
            velocity=(0, 0),
        )

        game_ended = False
        while not game_ended:
            for event in pygame.event.get():
                # Check if user clicks X button in window
                if event.type == pygame.QUIT:
                    game_ended = True

            # Fill screen with default background color
            self.screen.fill(self.bg_color)

            # Draw temp walls
            walls = []
            for row_idx, row in enumerate(self.temp_map):
                for col_idx, col in enumerate(row):
                    if col == "x":
                        walls.append(
                            pygame.Rect(
                                col_idx * self.temp_tile_size,
                                row_idx * self.temp_tile_size,
                                self.temp_tile_size,
                                self.temp_tile_size,
                            ),
                        )

            r = Room(walls)
            r.position_walls(
                self.screen,
                (
                    hero.rect.centerx - self.screen.get_size()[0] // 2,
                    hero.rect.centery - self.screen.get_size()[1] // 2,
                ),
            )

            # Draw hero and update its position
            self.screen.blit(hero.image, hero.rect)
            hero.get_input()
            hero.move()

            # Update screen with recently drawn elements
            pygame.display.flip()

            # Keep a constant FPS rate
            self.clock.tick(self.fps)

        pygame.quit()
