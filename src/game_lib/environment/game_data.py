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
        font: pygame.font.Font,
    ) -> None:
        """Initialize GameData instance."""
        self.screen = screen
        self.clock = clock
        self.fps = fps
        self.bg_color = bg_color
        self.font = font

        self.hero = Hero(
            position=(800, 500),
            image_paths=["orc.png"],
            dimensions=(3 * 20, 3 * 32),
            base_speed=3,
            health_points=400,  # TODO: different classes can have different HPs and base attack forces
            damage_image="orc_dmg.png",
            idle_image="orc.png",
            attack_image="orc_atk.png",
        )

        # Instance the main room
        self.game_room = Room(walls=[], map_image_path="feup_map.png")

        # Get room dimensions
        w, h = self.game_room.map_rect.w, self.game_room.map_rect.h
        self.temp_tile_size = 10

        # Initialize 40 randomly instantiated enemies
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
                attack_image="bat.png",
                attack_force=1,
                rarity=0.5,
                is_follower=(3 * random()) < 1,  # Only occurs 33% of the time
            )
            for _ in range(40)
        ]

    def game_loop(self) -> None:
        """Run each iteration of the game at a constant frame rate."""
        game_ended = False
        total_enemies = len(self.enemies)
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
            alive_enemies = []
            for enemy in self.enemies:
                # Draw and update it
                self.draw(enemy.image, enemy.rect)
                enemy.update_movement(self.hero)

                # Check for attacks against hero
                self.hero.check_attack(enemy, enemy.attack_force)

                if not enemy.is_dead:
                    alive_enemies.append(enemy)

            self.enemies = alive_enemies

            # Display HP
            self.screen.blit(
                self.font.render(f'HP {self.hero.health_points}', True, 'White'), (10, 10)
            )
            # Display points
            self.screen.blit(
                self.font.render(f'Points {5 * (total_enemies - len(self.enemies))}', True, 'White'),
                (self.screen.get_width() - 400, self.screen.get_height() - 50)
            )

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
