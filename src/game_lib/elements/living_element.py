"""Any MovingElement that has health points."""
from typing import Tuple
from .moving_element import MovingElement
from ..utils.engine import load_png
from constants.living_states import IDLE, REST, WALK, ATTACK, DIE, state_str
import pygame


class LivingElement(MovingElement):
    """Any MovingElement that has health points."""

    def __init__(
        self,
        position: Tuple[int, int],
        image_paths: list[str],
        dimensions: Tuple[int, int],
        base_speed: int,
        health_points: int,
        damage_image: str,
        idle_image: str,
        attack_image: str,
        can_fly: bool = False,
    ) -> None:
        """Initialize LivingElement instance."""
        super().__init__(position, image_paths, dimensions, base_speed, can_fly)
        self.is_dead = False
        self.health_points = health_points
        self.damage_image = pygame.transform.scale(
            load_png(damage_image)[0], self.dimensions
        )
        self.idle_image = pygame.transform.scale(
            load_png(idle_image)[0], self.dimensions
        )
        self.attack_image = pygame.transform.scale(
            load_png(attack_image)[0], self.dimensions
        )

        self.state = IDLE
        self.state_idx = 0
        self.cooldown_frames = 0

    def check_attack(self, opponent: "LivingElement", attack_force: int) -> None:
        """Check if attacked and decrease health points."""
        if self.is_colliding(opponent):
            if opponent.state == ATTACK:
                self.health_points -= attack_force
                self.image = self.damage_image
                self.cooldown_frames = 8

            if self.state == ATTACK:
                opponent.health_points -= attack_force
                opponent.image = opponent.damage_image
            else:
                opponent.image = opponent.idle_image

        # Set is_dead when element runs out of hp
        if self.health_points <= 0:
            self.health_points = 0
            self.is_dead = True

        # Set is_dead when element runs out of hp
        if opponent.health_points <= 0:
            opponent.health_points = 0
            opponent.is_dead = True

        # Return to idle image when cooldown is reached
        if self.state == ATTACK:
            self.image = self.attack_image
        elif self.cooldown_frames == 0:
            self.image = self.idle_image
        else:
            self.cooldown_frames -= 1

    def heal(self, hp: int) -> None:
        """Heal living element increasing health points."""
        pass
