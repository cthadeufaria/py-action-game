"""Any MovingElement that has health points."""
from typing import Tuple
from .moving_element import MovingElement
from ..utils.engine import load_png
from ..constants.living_states import IDLE, REST, ATTACK, DIE, state_str
from ..constants.colors import BLACK, RED, GREEN
import pygame
import os

NUM_STATES = 10


class LivingElement(MovingElement):
    """Any MovingElement that has health points."""

    def __init__(
        self,
        position: Tuple[int, int],
        role: str,
        dimensions: Tuple[int, int],
        base_speed: int,
        health_points: int,
        can_fly: bool = False,
    ) -> None:
        """Initialize LivingElement instance."""
        super().__init__(
            position,
            os.path.join("characters", role, "walk_0.png"),
            dimensions,
            base_speed,
            can_fly,
        )
        self.role = role
        self.max_health_points = health_points
        self.health_points = health_points

        self.images_by_state = [
            [
                pygame.transform.scale(
                    load_png(
                        os.path.join(
                            "characters", role, f"{state_name}_{state_index}.png"
                        )
                    )[0],
                    self.dimensions,
                )
                for state_index in range(NUM_STATES)
            ]
            for state_name in state_str
        ]

        self.state = IDLE
        self.state_idx = 0
        self.state_cooldown = 0
        self.cooldown_frames = 0
        self.is_going_left = False

    def is_dead(self) -> bool:
        """Check if LivingElement is dead."""
        return self.state == DIE and self.state_idx == NUM_STATES - 1

    def get_damage(self, attack_force: int) -> None:
        """Decrease health points upon attack."""
        self.health_points -= attack_force
        if self.health_points <= 0:
            self.health_points = 0
            self.state = DIE
            self.state_idx = 0

    def heal(self, hp: int) -> None:
        """Heal living element increasing health points."""
        self.health_points = min(self.max_health_points, self.health_points + hp)

    def update_image(self) -> None:
        """Set element's image base on its current state."""
        self.image = self.images_by_state[self.state][self.state_idx]
        if self.state_cooldown == 2:
            # Determine next state based on previous state
            if self.health_points == 0:
                self.velocity = (0, 0)
                self.state = DIE
            elif self.state == ATTACK and self.state_idx == NUM_STATES - 1:
                self.state = IDLE
            elif self.state == IDLE and self.state_idx == NUM_STATES - 1:
                self.state = REST
            elif self.state == REST and self.state_idx == NUM_STATES - 1:
                self.state = IDLE
            self.state_cooldown = 0
            self.state_idx = (self.state_idx + 1) % NUM_STATES
        else:
            self.state_cooldown += 1

    def display_health_bar(
        self, screen: pygame.surface.Surface, offset: Tuple[int, int]
    ) -> None:
        """Draw a bar above the LivingElement that represents its current health points."""
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
