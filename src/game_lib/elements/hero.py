"""A LivingElement controlled by the player."""
from .living_element import LivingElement
from typing import Tuple


class Hero(LivingElement):
    """A LivingElement controlled by the player."""

    def __init__(
        self,
        position: Tuple[int, int],
        image_paths: list[str],
        dimensions: Tuple[int, int],
        base_speed: float,
        velocity: Tuple[int, int],
    ) -> None:
        """Initialize Hero instance."""
        super().__init__(position, image_paths, dimensions, base_speed, velocity)
