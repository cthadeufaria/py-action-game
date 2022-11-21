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
        health_points: int,
        damage_image: str,
        idle_image: str,
    ) -> None:
        """Initialize LivingElement instance."""
        super().__init__(position, image_paths, dimensions, base_speed)
        self.is_dead = False
        self.health_points = health_points
        self.damage_image = damage_image
        self.idle_image = idle_image
        self.is_attack = False

    def attack(self) -> None:
        self.is_attack = True

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
