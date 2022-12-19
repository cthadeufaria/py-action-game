"""Any LivingElement that can attack and be attacked by a Hero."""
from typing import Tuple
from random import randint, random
from .living_element import LivingElement
from ..utils.math import check_inside_circle
from .hero import Hero
from ..constants.living_states import IDLE, WALK, DIE
from ..constants.screen import FPS


class Enemy(LivingElement):
    """Any LivingElement that can attack and be attacked by a Hero."""

    def __init__(
        self,
        position: Tuple[int, int],
        role: str,
        dimensions: Tuple[int, int],
        base_speed: int,
        can_fly: bool,
        health_points: int,
        attack_force: int,
        is_follower: bool,
    ) -> None:
        """Initialize Enemy instance."""
        super().__init__(
            position,
            role,
            dimensions,
            base_speed,
            health_points,
            can_fly,
        )
        self.attack_force = attack_force
        self.is_follower = is_follower
        self.target = (0, 0)
        self.num_steps = 0
        self.initial_pos = position
        self.walking_radius = randint(400, 1200)

    def update_movement(self, hero: Hero) -> None:
        """Update enemy's position depending on its attributes."""
        # Dead enemies no not move
        if self.state == DIE:
            return

        # If enemy is a follower and player is inside radius, go towards player
        if self.is_follower:
            if check_inside_circle(
                hero.rect.center, self.initial_pos, self.walking_radius
            ):
                self.target = (hero.rect.centerx, hero.rect.centery)
            else:
                self.target = self.rect.center
                if self.state == WALK:
                    self.state = IDLE

        # If enemy is a wanderer or player is outside radius, walk randomly inside radius
        elif self.num_steps == 0:
            self.target = (
                self.initial_pos[0] + int((random() - 0.5) * self.walking_radius),
                self.initial_pos[1] + int((random() - 0.5) * self.walking_radius),
            )

        # Only change target point every second
        self.num_steps = (self.num_steps + 1) % FPS

        # Update velocity towards target
        norm_v = max(
            0.001,  # avoid division by zero
            (
                (self.target[0] - self.rect.centerx) ** 2
                + (self.target[1] - self.rect.centery) ** 2
            )
            ** 0.5,
        )

        if norm_v > 0.001:
            self.state = WALK

        self.velocity = (
            (self.target[0] - self.rect.centerx) / norm_v,
            (self.target[1] - self.rect.centery) / norm_v,
        )

        # Face correct side when velocity changes
        if self.velocity[0] < 0:
            self.is_going_left = True
        elif self.velocity[0] > 0:
            self.is_going_left = False
