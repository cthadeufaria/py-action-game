"""Any Element that can move on the game map."""
from .element import Element
from typing import Tuple
import pygame


class MovingElement(Element):
    """Any Element that can move on the game map."""

    def __init__(
        self,
        position: Tuple[int, int],
        base_image_path: str,
        dimensions: Tuple[int, int],
        base_speed: int,
        can_fly: bool = False,
    ) -> None:
        """Initialize MovingElement instance."""
        self.base_speed = base_speed
        self.velocity = (0, 0)
        self.can_fly = can_fly
        super().__init__(position, base_image_path, dimensions)

    def move(self, walls: list[pygame.Rect]) -> None:
        """Update the position of rect based on current velocity."""
        dx = self.base_speed * self.velocity[0]
        self.rect.x += dx

        # If element hits a wall horizontally, move it to its appropriate edge
        if not self.can_fly:
            for wall in walls:
                if wall.colliderect(self.rect):
                    if dx > 0:
                        self.rect.right = wall.left
                    if dx < 0:
                        self.rect.left = wall.right

        dy = self.base_speed * self.velocity[1]
        self.rect.y += dy

        # If element hits a wall vertically, move it to its appropriate edge
        if not self.can_fly:
            for wall in walls:
                if wall.colliderect(self.rect):
                    if dy > 0:
                        self.rect.bottom = wall.top
                    if dy < 0:
                        self.rect.top = wall.bottom
