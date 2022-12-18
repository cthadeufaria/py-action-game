"""Any MovingElement that draws health points from a LivingElement."""
from .moving_element import MovingElement
from typing import Tuple


class Projectile(MovingElement):
    """Any MovingElement that draws health points from a LivingElement."""

    def __init__(
        self,
        position: Tuple[int, int],
        base_image_path: str,
        dimensions: Tuple[int, int],
        base_speed: int,
        velocity: Tuple[int, int],
        attack_force: int,
    ) -> None:
        """Initialize Projectile instance."""
        self.attack_force = attack_force
        super().__init__(
            position, base_image_path, dimensions, base_speed, can_fly=True
        )
        self.velocity = velocity
        self.is_active = True
