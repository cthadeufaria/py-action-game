"""Class that stores state of the game environment."""
import os.path
from typing import Tuple
import pygame
from .room import Room
from ..elements.hero import Hero
from ..elements.enemy import Enemy
from random import randint, random
from constants.heroes import heroes
from constants.buttons import menus, menu_type


class GameData:
    """Class that stores state of the game environment."""

    def __init__(
        self,
        screen: pygame.surface.Surface,
        clock: pygame.time.Clock,
        fps: int,
        bg_color: Tuple[int, int, int],
        font: pygame.font.Font,
    ) -> None:
        """Initialize GameData instance."""
        self.screen = screen
        self.clock = clock
        self.fps = fps
        self.bg_color = bg_color
        self.font = font

        # Init temporary / default Hero
        self.hero = Hero(
            position=(800, 500),
            image_paths=["orc.png"],
            dimensions=(3 * 32, 3 * 32),
            base_speed=3,
            health_points=400,
            stamina=400,
            base_attack=10,
            damage_image="orc_dmg.png",
            idle_image="orc.png",
            attack_image="orc_atk.png",
        )

        # Set offset when drawing elements on screen relative to the hero
        self.blit_offset = (
            self.screen.get_size()[0] // 2 - self.hero.rect.centerx,
            self.screen.get_size()[1] // 2 - self.hero.rect.centery,
        )

        # Instance the main room
        self.game_room = Room(
            walls_file_path="walls.json", map_image_path="feup_map.png"
        )

        # Get room dimensions
        w, h = self.game_room.map_rect.w, self.game_room.map_rect.h
        self.temp_tile_size = 10

        # Initialize 40 randomly instantiated enemies
        # TODO: perhaps select difficulty level at the beginning and generate more/less enemies
        self.enemies = [
            Enemy(
                position=(randint(w // 8, 7 * w // 8), randint(h // 3, 2 * h // 3)),
                image_paths=["bat.png", "bat_dmg.png"],
                dimensions=(40, 40),
                base_speed=randint(5, 12),
                health_points=10,
                damage_image="bat_dmg.png",
                idle_image="bat.png",
                attack_image="bat.png",
                attack_force=1,
                rarity=0.5,
                is_follower=(3 * random()) < 1,  # Only occurs 33% of the time
                can_fly=True,
            )
            for _ in range(40)
        ]

    def change_hero(self, role: str) -> None:
        """Create new hero object based on selected role."""
        self.hero = Hero(
            position=(800, 500),
            image_paths=[os.path.join("heroes", role, "male", "walk_0.png")],
            dimensions=(3 * 32, 3 * 32),
            base_speed=heroes[role]["base_speed"],
            health_points=heroes[role]["health_points"],
            stamina=heroes[role]["stamina"],
            base_attack=heroes[role]["base_attack"],
            damage_image=os.path.join("heroes", role, "male", "die_3.png"),
            idle_image=os.path.join("heroes", role, "male", "walk_3.png"),
            attack_image=os.path.join("heroes", role, "male", "attack_3.png"),
        )

    def menu_loop(self, menu_name: str) -> str:
        """Loop main menu, pause menu and game over screens."""
        mouse: Tuple[int, int]
        rects: list[pygame.Rect]

        menu: menu_type = menus[menu_name]

        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()

        button_options = menu["options"]
        rects = []

        # Create list with one rectangle for each button
        for idx in range(len(button_options)):
            rects.append(
                pygame.Rect(
                    screen_width // 2 - menu["button_width"] // 2,
                    screen_height // 2
                    + (idx - len(button_options) // 2) * menu["button_height"]
                    + (idx - len(button_options) // 2) * menu["buttons_spacement"],
                    menu["button_width"],
                    menu["button_height"],
                )
            )

        while True:
            # fills the screen with a color - TODO: put image instead
            self.screen.fill((50, 50, 50))

            # stores the (x,y) coordinates into the variable as a tuple
            mouse = pygame.mouse.get_pos()

            for event in pygame.event.get():
                # Check if user clicks X button in window
                if event.type == pygame.QUIT:
                    return "quit"

                # Check if a mouse is clicked
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for rect in rects:
                        # Return text correspondent to clicked button
                        if pygame.Rect.collidepoint(rect, mouse):
                            return button_options[rects.index(rect)].lower()

            # If mouse is hovered on a button it changes to lighter shade
            for rect in rects:
                if pygame.Rect.collidepoint(rect, mouse):
                    pygame.draw.rect(self.screen, menu["color_light"], rect, 0)
                else:
                    pygame.draw.rect(self.screen, menu["color_dark"], rect, 0)

                # Draw the text in the middle of button
                button_text = self.font.render(
                    button_options[rects.index(rect)], True, menu["color_text"]
                )
                self.screen.blit(
                    button_text,
                    (
                        rect.centerx - button_text.get_width() // 2,
                        rect.centery - button_text.get_height() // 2,
                    ),
                )

            # Update screen with recently drawn elements
            pygame.display.flip()

            # Keep a constant FPS rate
            self.clock.tick(self.fps)

    def game_loop(self) -> str:
        """Run each iteration of the game at a constant frame rate."""
        total_enemies = len(self.enemies)
        while True:
            for event in pygame.event.get():
                # Check if user clicks X button in window
                if event.type == pygame.QUIT:
                    return "quit"

            # Update drawing offset
            self.blit_offset = (
                self.screen.get_size()[0] // 2 - self.hero.rect.centerx,
                self.screen.get_size()[1] // 2 - self.hero.rect.centery,
            )

            # Fill screen with default background color
            self.screen.fill(self.bg_color)

            # Draw game map
            self.draw(self.game_room.map_surface, self.game_room.map_rect)

            # Draw hero and update its position
            if self.hero.is_going_left:
                self.draw(
                    pygame.transform.flip(self.hero.image, True, False), self.hero.rect
                )
            else:
                self.draw(self.hero.image, self.hero.rect)

            self.hero.get_input()
            self.hero.move(self.game_room.walls)
            self.hero.display_health_bar(self.screen, self.blit_offset)

            # For each enemy
            alive_enemies = []
            for enemy in self.enemies:
                # Draw and update it
                self.draw(enemy.image, enemy.rect)
                enemy.update_movement(self.hero)

                # Check for attacks against hero
                self.hero.check_attack(enemy, enemy.attack_force)

                enemy.display_health_bar(self.screen, self.blit_offset)

                if not enemy.is_dead():
                    alive_enemies.append(enemy)

            self.enemies = alive_enemies

            self.game_room.position_walls(self.screen, self.hero)

            # Display stamina
            self.screen.blit(self.font.render("Stamina", True, "White"), (10, 10))
            self.hero.display_stamina_bar(self.screen)

            # Display points
            self.screen.blit(
                self.font.render(
                    f"Points {5 * (total_enemies - len(self.enemies))}", True, "White"
                ),
                (self.screen.get_width() - 400, self.screen.get_height() - 50),
            )

            # Update screen with recently drawn elements
            pygame.display.flip()

            # Keep a constant FPS rate
            self.clock.tick(self.fps)

            # get pressed keys
            keys = pygame.key.get_pressed()

            # Enter game over screen based on health_points value
            if self.hero.health_points <= 0:
                return "game_over"

            # Press escape key to enter pause menu
            elif keys[pygame.K_ESCAPE]:
                return "pause"

    def draw(self, image: pygame.surface.Surface, rect: pygame.rect.Rect) -> None:
        """Position everything on screen depending on player's position."""
        self.screen.blit(
            image,
            (
                rect.topleft[0] + self.blit_offset[0],
                rect.topleft[1] + self.blit_offset[1],
            ),
        )
