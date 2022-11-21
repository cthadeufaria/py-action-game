"""Class that stores state of the game environment."""
from typing import Tuple
import pygame
from .room import Room
from ..elements.hero import Hero
from ..elements.enemy import Enemy
from random import choice, randint, random


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
            dimensions=(3 * 20, 3 * 32),
            base_speed=3,
            health_points=15,
            damage_image="orc_dmg.png",
            idle_image="orc.png",
        )

        # Get screen dimensions
        w, h = pygame.display.get_surface().get_size()
        self.temp_tile_size = 10

        # Initialize 10 randomly instantiated enemies
        # TODO: perhaps select difficulty level at the beginning and generate more/less enemies
        self.enemies = [
            Enemy(
                position=(randint(w // 8, 7 * w // 8), randint(h // 3, 2 * h // 3)),
                image_paths=["bat.png", "bat_dmg.png"],
                dimensions=(40, 40),
                base_speed=randint(5, 12),
                health_points=10,
                damage_image="bat_dmg.png",
                idle_image="bat.png",
                attack_force=5,
                rarity=0.5,
                is_follower=(3 * random()) < 1,  # Only occurs 33% of the time
            )
            for _ in range(10)
        ]

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
            if self.hero.is_going_left:
                self.draw(
                    pygame.transform.flip(self.hero.image, True, False), self.hero.rect
                )
            else:
                self.draw(self.hero.image, self.hero.rect)
            self.hero.get_input()
            self.hero.move()

            # For each enemy
            for enemy in self.enemies:
                # Draw and update it
                self.draw(enemy.image, enemy.rect)
                enemy.update_movement(self.hero)

                # Check for attacks against hero
                self.hero.check_attack(enemy, enemy.attack_force)

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
                rect.topleft[0]
                - self.hero.rect.centerx
                + self.screen.get_size()[0] // 2,
                rect.topleft[1]
                - self.hero.rect.centery
                + self.screen.get_size()[1] // 2,
            ),
        )
