"""A LivingElement controlled by the player."""
from typing import Tuple
from .living_element import LivingElement
import pygame.key
from math import sqrt


class Hero(LivingElement):
    """A LivingElement controlled by the player."""

    def __init__(
        self,
        position: Tuple[int, int],
        image_paths: list[str],
        dimensions: Tuple[int, int],
        base_speed: int,
        velocity: Tuple[int, int],
    ) -> None:
        """Initialize Hero instance."""
        super().__init__(position, image_paths, dimensions, base_speed, velocity)

    def get_input(self) -> None:
        """Change speed velocity based on keys pressed."""
        keys = pygame.key.get_pressed()

        # Press period key to run
        mod_speed = self.base_speed
        if keys[pygame.K_PERIOD]:
            mod_speed *= 2

        vx, vy = 0, 0

        # Allow moving with WASD or arrow keys
        if keys[pygame.K_UP or pygame.K_w]:
            vy = -mod_speed
        if keys[pygame.K_RIGHT or pygame.K_d]:
            vx = mod_speed
        if keys[pygame.K_DOWN or pygame.K_s]:
            vy = mod_speed
        if keys[pygame.K_LEFT or pygame.K_a]:
            vx = -mod_speed

        # Assign velocity, and normalize if necessary
        self.velocity = (vx, vy)
        if vx != 0 and vy != 0:
            self.velocity = (
                round(mod_speed * vx / sqrt(vx**2 + vy**2)),
                round(mod_speed * vy / sqrt(vx**2 + vy**2)),
            )
