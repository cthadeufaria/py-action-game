"""A LivingElement controlled by the player."""
from typing import Tuple
from .living_element import LivingElement
from .equipable import Equipable
from .projectile import Projectile
from ..constants.living_states import IDLE, WALK, ATTACK, DIE
from ..constants.colors import BLACK, RED, GREEN
from ..utils.sound import hero_cry
import pygame.key
from math import sqrt


class Hero(LivingElement):
    """A LivingElement controlled by the player."""

    def __init__(
        self,
        position: Tuple[int, int],
        role: str,
        dimensions: Tuple[int, int],
        base_speed: int,
        health_points: int,
        stamina: int,
        base_attack: int,
    ) -> None:
        """Initialize Hero instance."""
        super().__init__(
            position,
            role,
            dimensions,
            base_speed,
            health_points,
        )
        self.state = IDLE
        self.max_stamina = stamina
        self.stamina = stamina
        self.is_recovering = False
        self.is_shooter = role in ["ranger", "wizard"]
        self.projectile_image = f"{role}_projectile.png"

        # TODO: change/refactor to simpler weapon structure
        self.current_weapon = Equipable(
            position, "ball.png", (10, 10), 0.1, base_attack, 1
        )
        self.inventory: list[Equipable] = []

    def equip(self, eq_number: int) -> None:
        """Equip equipable to use."""
        self.current_weapon = self.inventory[eq_number]

    def get_input(self) -> None:
        """Change speed velocity based on keys pressed."""
        # Dead heroes should not move
        if self.state == DIE:
            return

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
        if keys[pygame.K_v]:
            self.state = ATTACK

        # Assign velocity, and normalize if necessary
        self.velocity = (vx, vy)
        if vx != 0 and vy != 0:
            self.velocity = (
                round(mod_speed * vx / sqrt(vx**2 + vy**2)),
                round(mod_speed * vy / sqrt(vx**2 + vy**2)),
            )

        # Assign walking state
        if vx != 0 or vy != 0:
            self.state = WALK
        elif self.state == WALK:
            self.state = IDLE

    def check_attack(self, opponent: "LivingElement", attack_force: int) -> None:
        """Check if attacked and decrease health points."""
        if self.is_colliding(opponent) and not opponent.state == DIE:
            opponent.state = ATTACK
            if self.state == ATTACK:
                opponent.get_damage(self.current_weapon.attack_force)
            elif opponent.state_idx == 6:
                self.get_damage(attack_force)
                self.cooldown_frames = 8
                hero_cry()

    def shoot(self) -> Projectile | None:
        """Create a new Projectile object on the game map."""
        if self.state == ATTACK and self.state_idx == 6 and self.state_cooldown == 0:
            return Projectile(
                position=self.rect.midleft
                if self.is_going_left
                else self.rect.midright,
                dimensions=(60, 15),
                attack_force=self.current_weapon.attack_force,
                base_image_path=self.projectile_image,
                velocity=(-1, 0) if self.is_going_left else (1, 0),
                base_speed=12,
            )
        else:
            return None

    def display_stamina_bar(self, screen: pygame.surface.Surface) -> None:
        """Draw a bar on screen that represents current hero stamina."""
        bar_size = (100, 20)
        stamina_bar_rect = pygame.Rect(120, 10, *bar_size)
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
