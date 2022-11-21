"""Any Element that can move on the game map."""
from .element import Element
from typing import Tuple


class MovingElement(Element):
    """Any Element that can move on the game map."""

    def __init__(
        self,
        position: Tuple[int, int],
        image_paths: list[str],
        dimensions: Tuple[int, int],
        base_speed: int,
    ) -> None:
        """Initialize MovingElement instance."""
        self.base_speed = base_speed
        self.velocity = (0, 0)
        super().__init__(position, image_paths, dimensions)

    def move(self) -> None:
        """Update the position of rect based on current velocity."""
        dx = self.base_speed * self.velocity[0]
        dy = self.base_speed * self.velocity[1]
        self.rect.center = (
            self.rect.center[0] + dx,
            self.rect.center[1] + dy,
        )
