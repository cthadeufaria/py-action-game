"""A LivingElement controlled by the player."""
from typing import Tuple
from .living_element import LivingElement
from .equipable import Equipable
from constants.living_states import IDLE, REST, WALK, ATTACK, DIE, state_str
from constants.colors import BLACK, RED, GREEN
import pygame.key
from math import sqrt


class Hero(LivingElement):
    """A LivingElement controlled by the player."""

    def __init__(
        self,
        position: Tuple[int, int],
        image_paths: list[str],
        dimensions: Tuple[int, int],
        base_speed: int,
        health_points: int,
        stamina: int,
        base_attack: int,
        damage_image: str,
        idle_image: str,
        attack_image: str,
    ) -> None:
        """Initialize Hero instance."""
        super().__init__(
            position,
            image_paths,
            dimensions,
            base_speed,
            health_points,
            damage_image,
            idle_image,
            attack_image,
        )
        self.state = IDLE
        self.is_going_left = False
        self.max_stamina = stamina
        self.stamina = stamina
        self.is_recovering = False

        # TODO: change/refactor to simpler weapon structure
        self.current_weapon = Equipable(position, ["ball.png"], (10, 10), 0.1, base_attack, 1)
        self.inventory: list[Equipable] = []

    def equip(self, eq_number: int) -> None:
        """Equip equipable to use."""
        self.current_weapon = self.inventory[eq_number]

    def get_input(self) -> None:
        """Change speed velocity based on keys pressed."""
        keys = pygame.key.get_pressed()

        # Press period key to run
        mod_speed = self.base_speed
        if keys[pygame.K_SPACE] and self.stamina > 0 and not self.is_recovering:
            mod_speed *= 2
            self.stamina -= 5
        else:
            self.stamina = min(self.max_stamina, self.stamina + 1)
            self.is_recovering = self.stamina < self.max_stamina // 4

        vx, vy = 0, 0

        # Allow moving with WASD or arrow keys
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            vy = -mod_speed
            # TODO: set integer value to select image in array
            self.is_going_left = False
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            vx = mod_speed
            self.is_going_left = False
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            vy = mod_speed
            self.is_going_left = False
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            vx = -mod_speed
            self.is_going_left = True

        # Verify if hero wants to attack
        self.state = ATTACK if keys[pygame.K_v] else IDLE

        if self.state == ATTACK:
            self.image = self.attack_image
        else:
            self.image = self.idle_image

        # Assign velocity, and normalize if necessary
        self.velocity = (vx, vy)
        if vx != 0 and vy != 0:
            self.state = WALK
            self.velocity = (
                round(mod_speed * vx / sqrt(vx**2 + vy**2)),
                round(mod_speed * vy / sqrt(vx**2 + vy**2)),
            )

    def check_attack(self, opponent: "LivingElement", attack_force: int) -> None:
        """Check if attacked and decrease health points."""
        if self.is_colliding(opponent):
            if self.state == ATTACK:
                opponent.image = opponent.damage_image
                opponent.get_damage(self.current_weapon.attack_force)
            else:
                self.get_damage(attack_force)
                opponent.image = opponent.idle_image
                self.image = self.damage_image
                self.cooldown_frames = 8

        # Return to idle image when cooldown is reached
        if self.state == ATTACK:
            self.image = self.attack_image
        elif self.cooldown_frames == 0:
            self.image = self.idle_image
        else:
            self.cooldown_frames -= 1

    def display_stamina_bar(self, screen: pygame.surface.Surface) -> None:
        """Draw a bar on screen that represents current hero stamina."""
        bar_size = (100, 20)
        stamina_bar_rect = pygame.Rect(200, 15, *bar_size)
        pygame.draw.rect(
            screen, RED, (stamina_bar_rect.x, stamina_bar_rect.y, *bar_size)
        )
        pygame.draw.rect(
            screen, BLACK, (stamina_bar_rect.x, stamina_bar_rect.y, *bar_size), 1
        )
        pygame.draw.rect(
            screen,
            GREEN,
            (
                stamina_bar_rect.x + 1,
                stamina_bar_rect.y + 1,
                int((bar_size[0] - 2) * self.stamina / self.max_stamina),
                bar_size[1] - 2,
            ),
        )
