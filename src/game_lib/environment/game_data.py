"""Class that stores state of the game environment."""
from typing import Tuple
import pygame


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
                ["x", *[" " for _ in range(-2 + w // self.temp_tile_size)], "x"]
                for _ in range(-2 + h // self.temp_tile_size)
            ],
            ["x" for _ in range(w // self.temp_tile_size)],
        ]

        # Generate temp particles
        from random import random

        self.temp_particles_positions = [
            [
                self.temp_tile_size + int(random() * w),
                self.temp_tile_size + int(random() * h),
            ]
            for _ in range(20)
        ]
        self.temp_particle_velocities = [
            ((random() - 0.5) * 4, (random() - 0.5) * 4) for _ in range(20)
        ]

    def game_loop(self) -> None:
        """Run each iteration of the game at a constant frame rate."""
        game_ended = False
        while not game_ended:
            for event in pygame.event.get():
                # Check if user clicks X button in window
                if event.type == pygame.QUIT:
                    game_ended = True

            # Fill screen with default background color
            self.screen.fill(self.bg_color)

            # Draw temp walls
            for row_idx, row in enumerate(self.temp_map):
                for col_idx, col in enumerate(row):
                    if col == "x":
                        pygame.draw.rect(
                            self.screen,
                            "red",
                            pygame.Rect(
                                col_idx * self.temp_tile_size,
                                row_idx * self.temp_tile_size,
                                self.temp_tile_size,
                                self.temp_tile_size,
                            ),
                        )

            # Update particles positions
            for p_idx in range(20):
                self.temp_particles_positions[p_idx][
                    0
                ] += self.temp_particle_velocities[p_idx][0]
                self.temp_particles_positions[p_idx][
                    1
                ] += self.temp_particle_velocities[p_idx][1]

                # Draw particles
                pygame.draw.rect(
                    self.screen,
                    "blue",
                    pygame.Rect(
                        self.temp_particles_positions[p_idx][0],
                        self.temp_particles_positions[p_idx][1],
                        self.temp_tile_size,
                        self.temp_tile_size,
                    ),
                )

            # Update screen with recently drawn elements
            pygame.display.flip()

            # Keep a constant FPS rate
            self.clock.tick(self.fps)

        pygame.quit()
