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
        base_speed: int,
        velocity: Tuple[int, int],
        health_points: int,
        damage_image: str,
        idle_image: str,
    ) -> None:
        """Initialize LivingElement instance."""
        self.health_points = health_points
        self.damage_image = damage_image
        self.idle_image = idle_image
        super().__init__(position, image_paths, dimensions, base_speed, velocity)

    def attack(self) -> None:
        pass

    def damaged(self) -> int:
        pass

    def is_dead(self) -> bool:
        pass
