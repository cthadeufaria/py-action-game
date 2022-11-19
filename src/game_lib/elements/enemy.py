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
        base_speed: int,
        velocity: Tuple[int, int],
        health_points: int,
        damage_image: str,
        idle_image: str,
        attack_force: int,
        rarity: float,
        is_follower: bool,
    ) -> None:
        """Initialize Enemy instance."""
        super().__init__(
            position,
            image_paths,
            dimensions,
            base_speed,
            velocity,
            health_points,
            damage_image,
            idle_image,
        )
        self.attack_force = attack_force
        self.rarity = rarity
        self.is_follower = is_follower

    def update_movement(self) -> None:
        """Implement aleatory enemie's movement."""
        pass
