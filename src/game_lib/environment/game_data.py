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

        self.hero = Hero(
            position=(800, 500),
            image_paths=["orc.png"],
            dimensions=(3*20, 3*32),
            base_speed=3,
            velocity=(0, 0),
        )

        # Get screen dimensions
        w, h = pygame.display.get_surface().get_size()
        self.temp_tile_size = 10

        # Generate temp map
        temp_map: list[list[str]] = [
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

        # Draw temp walls
        walls = []
        for row_idx, row in enumerate(temp_map):
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

        self.game_room = Room(walls=walls, map_image_path="feup_map.png")

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

            # Draw game map
            self.draw(self.game_room.map_surface, self.game_room.map_rect)

            # Draw hero and update its position
            if self.hero.going_left:
                self.draw(pygame.transform.flip(self.hero.image, True, False), self.hero.rect)
            else:
                self.draw(self.hero.image, self.hero.rect)
            self.hero.get_input()
            self.hero.move()

            # Update screen with recently drawn elements
            pygame.display.flip()

            # Keep a constant FPS rate
            self.clock.tick(self.fps)

        pygame.quit()

    def draw(self, image: pygame.surface.Surface, rect: pygame.rect.Rect) -> None:
        """Position everything on screen depending on player's position."""
        self.screen.blit(
            image,
            (
                rect.topleft[0] - self.hero.rect.centerx + self.screen.get_size()[0] // 2,
                rect.topleft[1] - self.hero.rect.centery + self.screen.get_size()[1] // 2,
            ),
        )
