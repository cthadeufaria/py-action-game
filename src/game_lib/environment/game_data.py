"""Class that stores state of the game environment."""
from typing import Tuple
import pygame
from .room import Room
from ..elements.hero import Hero
from ..elements.enemy import Enemy
from random import randint, random
import constants.buttons  # import main_menu, pause_menu, game_over_menu, hero_selection_menu
import constants.heroes  # import heroes


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
        self.hero: Hero
        self.screen = screen
        self.clock = clock
        self.fps = fps
        self.bg_color = bg_color
        self.font = font
        self.game_ended = False
        self.menu_ended = False
        self.pause = False
        self.game_over = False
        self.hero_selection = False
        self.is_quit = False

        # Instance the main room
        self.game_room = Room(walls=[], map_image_path="feup_map.png")

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
            )
            for _ in range(40)
        ]

    def hero_select(self, word: str) -> None:
        """Select hero class to play with."""
        hero = constants.heroes.heroes[word] # todo: insert more classes in constants.heroes to play with
        self.hero = Hero(
            position=hero["position"],
            image_paths=hero["image_paths"],
            dimensions=hero["dimensions"],
            base_speed=hero["base_speed"],
            health_points=hero[
                "health_points"
            ],  # TODO: different classes can have different HPs and base attack forces
            damage_image=hero["damage_image"],
            idle_image=hero["idle_image"],
            attack_image=hero["attack_image"],
        )
        self.hero_selection = False

    def menu_loop(self) -> None:
        """Loop main menu, pause menu and game over screens."""
        mouse: Tuple[int, int]
        rects: list[pygame.Rect]

        # Menu variables
        if self.pause:
            menu = constants.buttons.pause_menu
            self.pause = False
        elif self.game_over:
            menu = constants.buttons.game_over_menu
        elif self.hero_selection:
            menu = constants.buttons.hero_selection_menu
        else:
            menu = constants.buttons.main_menu

        width = self.screen.get_width()
        height = self.screen.get_height()
        buttons_placement = (width / 2, height / 2)
        smallfont = pygame.font.SysFont("Corbel", 35)

        color = menu["color"]
        color_light = menu["color_light"]
        color_dark = menu["color_dark"]
        buttons_spacement = menu["buttons_spacement"]
        button_width = menu["button_width"]
        button_height = menu["button_height"]
        words = menu["words"]
        rects = []

        # create list of rectangles
        for i in [item for item in range(len(words))]:
            rects.append(
                pygame.Rect(
                    buttons_placement[0] - button_width / 2,
                    buttons_placement[1]
                    + (i) * button_height
                    + (i) * buttons_spacement,
                    button_width,
                    button_height,
                )
            )

        while not self.menu_ended and not self.game_ended:
            # fills the screen with a color
            self.screen.fill((60, 25, 60))
            # stores the (x,y) coordinates into the variable as a tuple
            mouse = pygame.mouse.get_pos()

            for event in pygame.event.get():
                # Check if user clicks X button in window
                if event.type == pygame.QUIT:
                    self.game_ended = True
                    return False

                # Check if a mouse is clicked
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for rect in rects:
                        if pygame.Rect.collidepoint(rect, mouse):
                            if words[rects.index(rect)] == "Quit":
                                self.game_ended = True
                                return False
                            if words[rects.index(rect)] == "Play Now":
                                try:
                                    type(self.hero) == Hero
                                except AttributeError:
                                    self.hero_selection = True
                                self.menu_ended = True
                            elif words[rects.index(rect)] == 'Resume':
                                self.menu_ended = True
                            elif words[rects.index(rect)] == 'Play Again':
                                self.menu_ended = False
                                return False
                            elif words[rects.index(rect)] == "Options":
                                self.game_ended = True  # todo: Create options menu
                                return False
                            elif (
                                words[rects.index(rect)]
                                in constants.buttons.hero_selection_menu["words"]
                            ):
                                self.menu_ended = True
                                self.hero_select(words[rects.index(rect)])

            # if mouse is hovered on a button it changes to lighter shade
            for rect in rects:
                if pygame.Rect.collidepoint(rect, mouse):
                    pygame.draw.rect(self.screen, color_light, rect, 0)
                else:
                    pygame.draw.rect(self.screen, color_dark, rect, 0)

                # superimposing the text onto button
                self.screen.blit(
                    smallfont.render(words[rects.index(rect)], True, color),
                    (rect[0] + (rect[2] / 2), rect[1] + (rect[3] / 2)),
                )

            # updates the frames of the game
            pygame.display.update()

        if self.is_quit == True:
            return False

        if self.hero_selection == True:
            self.menu_ended = False
            self.menu_loop()

    def game_loop(self) -> None:
        """Run each iteration of the game at a constant frame rate."""
        total_enemies = len(self.enemies)
        while not self.game_ended:
            for event in pygame.event.get():
                # Check if user clicks X button in window
                if event.type == pygame.QUIT:
                    self.is_quit = True
                    return self.menu_loop()

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
            self.hero.move()

            # For each enemy
            alive_enemies = []
            for enemy in self.enemies:
                # Draw and update it
                self.draw(enemy.image, enemy.rect)
                enemy.update_movement(self.hero)

                # Check for attacks against hero
                self.hero.check_attack(enemy, enemy.attack_force)

                if not enemy.is_dead:
                    alive_enemies.append(enemy)

            self.enemies = alive_enemies

            # Display HP
            self.screen.blit(
                self.font.render(f"HP {self.hero.health_points}", True, "White"),
                (10, 10),
            )
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
                self.game_over = True
                self.menu_ended = False
                return self.menu_loop()
            # Press escape key to enter pause menu
            elif keys[pygame.K_ESCAPE]:
                self.pause = True
                self.menu_ended = False
                self.menu_loop()

        pygame.quit()

    def draw(self, image: pygame.surface.Surface, rect: pygame.rect.Rect) -> None:
        """Position everything on screen depending on player's position."""
        self.screen.blit(
            image,
            (
                rect.topleft[0]
                - self.hero.rect.centerx
                + self.screen.get_size()[0] // 2,
                rect.topleft[1]
                - self.hero.rect.centery
                + self.screen.get_size()[1] // 2,
            ),
        )
