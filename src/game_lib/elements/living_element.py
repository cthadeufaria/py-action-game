"""Any MovingElement that has health points."""
from .moving_element import MovingElement
from typing import Tuple


class LivingElement(MovingElement):
    """Any MovingElement that has health points."""

    def __init__(
        self,
        position: Tuple[int, int],
        image_paths: list[str],
        dimensions: Tuple[int, int],
        base_speed: float,
        velocity: Tuple[int, int],
    ) -> None:
        """Initialize LivingElement instance."""
        super().__init__(position, image_paths, dimensions, base_speed, velocity)
