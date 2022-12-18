"""Entry point for the game."""

# Standard module imports
import os

# Third-party imports
import pygame

# Local imports
import constants.colors
import constants.screen
from constants.heroes import heroes
from game_lib.environment.game_data import GameData
from game_lib.utils.engine import get_absolute_path
import game_lib.environment.sound

# Center window
os.environ["SDL_VIDEO_CENTERED"] = "1"

# Initialize game engine
pygame.init()

# Set window name, size and default font
pygame.display.set_caption("FEUPscape")
screen = pygame.display.set_mode(constants.screen.dimensions["medium"])
font = pygame.font.Font(get_absolute_path(__file__, "assets", "wonder.ttf"), 25)

# Create clock for game loop
clock = pygame.time.Clock()

# Entry point, game loop
if __name__ == "__main__":
    state = "main_menu"
    last_state = state
    selected_role = "orc"
    game = GameData(
        screen=screen,
        clock=clock,
        fps=constants.screen.FPS,
        bg_color=constants.colors.GRASS,
        font=font,
    )

    while state != "exit":
        if state == "resume":
            state = game.game_loop()
        elif state == "play again":
            state = "main_menu"
        elif state == "main_menu":
            last_state = state
            state = game.menu_loop("main_menu")
        elif state == "play now":
            state = game.menu_loop("hero_selection_menu")
        elif state == "pause":
            last_state = state
            state = game.menu_loop("pause_menu")
        elif state == "game_over":
            game.change_hero(selected_role)
            state = game.menu_loop("game_over_menu")
        elif state in [h.lower() for h in heroes.keys()]:
            selected_role = state
            game.change_hero(selected_role)
            state = "resume"
        elif state == "options":
            state = game.menu_loop("options_menu")
        elif state == "quit":
            state = "main_menu"
        elif state == "volume up":
            game.volume_control("up")
            state = "options"
        elif state == "volume down":
            game.volume_control("down")
            state = "options"
        elif state == "back":
            state = last_state

    pygame.quit()
