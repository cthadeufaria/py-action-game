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
        base_speed: float,
        velocity: Tuple[int, int],
    ) -> None:
        """Initialize MovingElement instance."""
        self.base_speed = base_speed
        self.velocity = velocity
        super().__init__(position, image_paths, dimensions)

    def move(self) -> None:
        movement = list()  # type: list[float]
        dx = self.base_speed * self.velocity[0]
        dy = self.base_speed * self.velocity[1]
        self.rect.move(dx, dy)
