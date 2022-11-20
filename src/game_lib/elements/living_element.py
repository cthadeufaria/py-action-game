"""Any MovingElement that has health points."""
from .moving_element import MovingElement
from typing import Tuple
import pygame


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
        self.is_dead: bool
        self.is_attack: bool
        self.health_points = health_points
        self.damage_image = damage_image
        self.idle_image = idle_image
        super().__init__(position, image_paths, dimensions, base_speed, velocity)

    def attack(self) -> None:
        """Attack enemies."""
        pass

    def check_attack(
        self, rect: pygame.rect.Rect, attack_force: int, is_attack: bool
    ) -> None:
        """Check if attacked and decrease health points."""
        if self.is_colliding(rect) and is_attack:
            self.health_points -= attack_force
        if self.health_points <= 0:
            self.health_points = 0
            self.is_dead = True
        else:
            self.is_dead = False

    def heal(self, hp: int) -> None:
        """Heal living element increasing health points."""
        pass
