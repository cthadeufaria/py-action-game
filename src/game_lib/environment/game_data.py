"""Class that stores state of the game environment."""
import pygame
from random import randint, random, choice
from typing import Tuple, TypedDict
from .room import Room
from ..elements.collectable import Collectable
from ..elements.hero import Hero
from ..elements.enemy import Enemy
from ..universal.auth_player import AuthPlayer
from ..utils.engine import load_png
from ..constants.heroes import heroes
from ..constants.enemies import enemies
from ..constants.buttons import menus, menu_type
from ..utils.sound import set_volume, play_soundtrack


class GameData:
    """Class that stores state of the game environment."""

    def __init__(
        self,
        screen: pygame.surface.Surface,
        clock: pygame.time.Clock,
        fps: int,
        bg_color: Tuple[int, int, int],
        font: pygame.font.Font,
        auth: AuthPlayer,
    ) -> None:
        """Initialize GameData instance."""
        self.screen = screen
        self.clock = clock
        self.fps = fps
        self.bg_color = bg_color
        self.font = font
        self.auth = auth
        self.db_cooldown = 0

        # Init temporary / default Hero
        self.hero = Hero(
            position=(800, 500),
            role="orc",
            dimensions=(3 * 32, 3 * 32),
            base_speed=3,
            health_points=400,
            stamina=400,
            base_attack=10,
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

        # Set game's base volume
        self.base_volume = 1.0

        # Get room dimensions
        w, h = self.game_room.map_rect.w, self.game_room.map_rect.h
        self.temp_tile_size = 10

        # Initialize randomly instantiated enemies
        enemies_type = TypedDict(
            "enemies_type",
            {
                "number": int,
                "dimensions": Tuple[int, int],
                "base_speed": int,
                "health_points": int,
                "attack_force": int,
                "can_fly": bool,
                "following_probability": float,
            },
        )
        enemies_dict: dict[str, enemies_type] = enemies  # type: ignore
        self.enemies = [
            Enemy(  # Final boss
                position=(4 * w // 5, h // 2),
                role="minotaur",
                dimensions=(400, 400),
                base_speed=2,
                health_points=300,
                attack_force=30,
                is_follower=True,
                can_fly=False,
            ),
            *[  # All other enemies
                Enemy(
                    position=(
                        choice(
                            [  # Position it either in chamber 1 or chamber 2
                                (randint(930, 3730), randint(360, 840)),
                                (randint(5040, 5450), randint(210, 1490)),
                            ]
                        )
                    ),
                    role=enemy_role,
                    dimensions=enemies_dict[enemy_role]["dimensions"],
                    base_speed=enemies_dict[enemy_role]["base_speed"],
                    health_points=enemies_dict[enemy_role]["health_points"],
                    attack_force=enemies_dict[enemy_role]["attack_force"],
                    is_follower=random()
                    < enemies_dict[enemy_role]["following_probability"],
                    can_fly=enemies_dict[enemy_role]["can_fly"],
                )
                for enemy_role in enemies_dict.keys()
                for _ in range(enemies_dict[enemy_role]["number"])
            ],
        ]

        # Initialize 3 randomly positioned potions in each chamber
        self.potions = [
            Collectable(
                position=[  # Position it either in chamber 1 or chamber 2
                    (randint(930, 3730), randint(360, 840)),
                    (randint(5040, 5450), randint(210, 1490)),
                ][chamber_index],
                base_image_path="potion.png",
                dimensions=(35, 35),
                rarity=0.5,
                heal_value=randint(100, 300),
            )
            for chamber_index in range(2)
            for _ in range(3)
        ]

    def change_hero(self, role: str) -> None:
        """Create new hero object based on selected role."""
        self.hero = Hero(
            position=(800, 500),
            role=role,
            dimensions=(3 * 32, 3 * 32),
            base_speed=heroes[role]["base_speed"],
            health_points=heroes[role]["health_points"],
            stamina=heroes[role]["stamina"],
            base_attack=heroes[role]["base_attack"],
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

        menu_image, _ = (
            load_png("roles_menu.png")
            if menu_name == "hero_selection_menu"
            else load_png("default_menu.png")
        )

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
            # Set background image
            self.screen.blit(menu_image, (0, 0))

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

    def volume_control(self, direction: str) -> None:
        """Change main base volume for each button click."""
        if direction == "up":
            self.base_volume = self.base_volume + 0.1
        elif direction == "down":
            self.base_volume = self.base_volume - 0.1
        set_volume(self.base_volume)

    def game_loop(self) -> str:
        """Run each iteration of the game at a constant frame rate."""
        total_enemies = len(self.enemies)
        active_projectiles = []
        play_soundtrack()
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
            self.hero.display_health_bar(self.screen, self.blit_offset)
            self.hero.move(self.game_room.walls)
            self.hero.update_image()

            # Generate shots
            if self.hero.is_shooter:
                new_projectile = self.hero.shoot()
                if new_projectile:
                    active_projectiles.append(new_projectile)

            # For each potion
            remaining_potions = []
            for potion in self.potions:
                # Draw and update it
                self.draw(potion.image, potion.rect)
                if self.hero.is_colliding(potion):
                    self.hero.heal(potion.heal_value)
                else:
                    remaining_potions.append(potion)
            self.potions = remaining_potions

            # For each enemy
            alive_enemies = []
            for enemy in self.enemies:
                # Draw and update it
                if enemy.is_going_left:
                    self.draw(
                        pygame.transform.flip(enemy.image, True, False), enemy.rect
                    )
                else:
                    self.draw(enemy.image, enemy.rect)

                enemy.update_movement(self.hero)
                enemy.move(self.game_room.walls)

                # Check for attacks against hero
                self.hero.check_attack(enemy, enemy.attack_force)

                # Check for projectiles colliding with enemy
                for projectile in active_projectiles:
                    if projectile.is_colliding(enemy):
                        enemy.get_damage(projectile.attack_force)
                        projectile.is_active = False

                enemy.display_health_bar(self.screen, self.blit_offset)
                enemy.update_image()

                if not enemy.is_dead():
                    alive_enemies.append(enemy)

            self.enemies = alive_enemies

            # Update and display each projectile
            remaining_projectiles = []
            for projectile in active_projectiles:
                projectile.move([])
                if (
                    projectile.rect.x > self.game_room.map_rect.w
                    or projectile.rect.x < 0
                ):
                    projectile.is_active = False
                self.draw(
                    pygame.transform.flip(
                        projectile.image, sum(projectile.velocity) == -1, False
                    ),
                    projectile.rect,
                )
                if projectile.is_active:
                    remaining_projectiles.append(projectile)
            active_projectiles = remaining_projectiles

            # Position invisible walls relative to the player
            self.game_room.position_walls(self.screen, self.hero)

            # Display stamina
            self.screen.blit(self.font.render("Stamina", True, "Red"), (10, 10))
            self.hero.display_stamina_bar(self.screen)

            # Display points
            self.screen.blit(
                self.font.render(
                    f"Your Points {5 * (total_enemies - len(self.enemies))}",
                    True,
                    "Red",
                ),
                (self.screen.get_width() - 200, self.screen.get_height() - 50),
            )
            for user_idx, user_id in enumerate(self.auth.ranking.keys()):
                self.screen.blit(
                    self.font.render(
                        f"{self.auth.ranking[user_id]['name']}: {self.auth.ranking[user_id]['points']}",
                        True,
                        "White",
                    ),
                    (
                        self.screen.get_width() - 200,
                        self.screen.get_height() - (50 * (2 + user_idx)),
                    ),
                )

            # Update screen with recently drawn elements
            pygame.display.flip()

            # Keep a constant FPS rate
            self.clock.tick(self.fps)

            # get pressed keys
            keys = pygame.key.get_pressed()

            # Enter game over screen when player is dead
            if self.hero.is_dead():
                return "game_over"

            # Press escape key to enter pause menu
            elif keys[pygame.K_ESCAPE]:
                return "pause"

            # Every 30 seconds update DB and query ranking
            self.db_cooldown += 1
            if self.db_cooldown > self.fps * 30:
                self.auth.query_ranking()
                self.auth.update_player_data(
                    points=5 * (total_enemies - len(self.enemies)),
                    pos=self.hero.position,
                )
                self.db_cooldown = 0

    def draw(self, image: pygame.surface.Surface, rect: pygame.rect.Rect) -> None:
        """Position everything on screen depending on player's position."""
        self.screen.blit(
            image,
            (
                rect.topleft[0] + self.blit_offset[0],
                rect.topleft[1] + self.blit_offset[1],
            ),
        )
