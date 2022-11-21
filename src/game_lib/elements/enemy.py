"""Any LivingElement that can attack and be attacked by a Hero."""
from typing import Tuple
from random import randint, random
from .living_element import LivingElement
from .hero import Hero


class Enemy(LivingElement):
    """Any LivingElement that can attack and be attacked by a Hero."""

    def __init__(
        self,
        position: Tuple[int, int],
        image_paths: list[str],
        dimensions: Tuple[int, int],
        base_speed: int,
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
            health_points,
            damage_image,
            idle_image,
        )
        self.attack_force = attack_force
        self.rarity = rarity
        self.is_follower = is_follower
        self.target = (0, 0)
        self.num_steps = 0
        self.initial_pos = position
        self.walking_radius = randint(400, 1200)

    def update_movement(self, hero: Hero) -> None:
        """Update enemy's position depending on its attributes."""
        # If enemy is a follower and player is inside radius, go towards player
        if self.is_follower and check_inside_circle(hero.rect.center, self.initial_pos, self.walking_radius):
            self.target = (hero.rect.centerx, hero.rect.centery)

        # If enemy is a wanderer or player is outside radius, walk randomly inside radius
        elif self.num_steps == 0:
            self.target = (
                self.initial_pos[0] + int((random() - 0.5) * self.walking_radius),
                self.initial_pos[1] + int((random() - 0.5) * self.walking_radius),
            )

        # Only change target point every second (30 FPS) - TODO: get from constants
        self.num_steps = (self.num_steps + 1) % 30

        # Update velocity towards target
        norm_v = max(
            0.001,  # avoid division by zero
            (
                (self.target[0] - self.rect.centerx) ** 2
                + (self.target[1] - self.rect.centery) ** 2
            )
            ** 0.5,
        )

        self.velocity = (
            (self.target[0] - self.rect.centerx) / norm_v,
            (self.target[1] - self.rect.centery) / norm_v,
        )

        self.move()


# CODE DUPLICATION - TODO: import from math.py utils file
def check_inside_circle(
    point: Tuple[int, int], center: Tuple[int, int], radius: int
) -> bool:
    """Determine if a circle defined by its center and radius contains a point."""
    return ((point[0] - center[0]) ** 2 + (point[1] - center[1]) ** 2) <= (radius**2)
