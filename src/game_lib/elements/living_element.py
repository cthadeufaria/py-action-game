"""Any MovingElement that has health points."""
from typing import Tuple
from .moving_element import MovingElement
from ..utils.engine import load_png
from constants.living_states import IDLE, REST, WALK, ATTACK, DIE, state_str
from constants.colors import BLACK, RED, GREEN
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
        self.max_health_points = health_points
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

    def is_dead(self) -> bool:
        """Check if LivingElement is dead."""
        return self.state == DIE

    def get_damage(self, attack_force: int) -> None:
        """Decrease health points upon attack."""
        self.health_points -= attack_force
        if self.health_points <= 0:
            self.health_points = 0
            self.state = DIE

    def heal(self, hp: int) -> None:
        """Heal living element increasing health points."""
        if hp >= (self.max_health_points - hp):
            self.health_points = self.max_health_points
        else:
            self.health_points += hp



    def display_health_bar(
        self, screen: pygame.surface.Surface, offset: Tuple[int, int]
    ) -> None:
        bar_size = (30, 10)

        health_bar_rect = pygame.Rect(0, 0, *bar_size)
        health_bar_rect.midbottom = self.rect.centerx, self.rect.top

        pygame.draw.rect(
            screen,
            RED,
            (health_bar_rect.x + offset[0], health_bar_rect.y + offset[1], *bar_size),
        )
        pygame.draw.rect(
            screen,
            BLACK,
            (health_bar_rect.x + offset[0], health_bar_rect.y + offset[1], *bar_size),
            1,
        )
        pygame.draw.rect(
            screen,
            GREEN,
            (
                health_bar_rect.x + 1 + offset[0],
                health_bar_rect.y + 1 + offset[1],
                int((bar_size[0] - 2) * self.health_points / self.max_health_points),
                bar_size[1] - 2,
            ),
        )

