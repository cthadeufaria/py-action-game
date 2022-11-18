"""Any LivingElement that can attack and be attacked by a Hero."""
from .living_element import LivingElement
from typing import Tuple


class Enemy(LivingElement):
    """Any LivingElement that can attack and be attacked by a Hero."""

    def __init__(
        self,
        position: Tuple[int, int],
        image_paths: list[str],
        dimensions: Tuple[int, int],
        base_speed: float,
        velocity: Tuple[int, int],
    ) -> None:
        """Initialize Enemy instance."""
        super().__init__(position, image_paths, dimensions, base_speed, velocity)
