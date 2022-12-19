"""Entry point for the game."""

# Standard module imports
import os

# Third-party imports
import pygame

# Local imports
from game_lib.constants import screen, colors, heroes
from game_lib.environment.game_data import GameData
from game_lib.utils.engine import get_absolute_path
from game_lib.utils.credentials import get_credentials, set_credentials
from game_lib.universal.auth_player import AuthPlayer

# import game_lib.environment.sound
from game_lib.universal.input_credentials import InputCredentials

# Center window
os.environ["SDL_VIDEO_CENTERED"] = "1"

# Initialize game engine
pygame.init()

# Set window name, size and default font
pygame.display.set_caption("FEUPscape")
game_screen = pygame.display.set_mode(screen.dimensions["medium"])
font = pygame.font.Font(get_absolute_path(__file__, "assets", "pixeboy.ttf"), 30)

# Create clock for game loop
clock = pygame.time.Clock()

# Entry point, game loop
if __name__ == "__main__":
    state = "main_menu"

    # Get user credentials and log user in
    auth = AuthPlayer("hero")
    credentials = get_credentials()
    if not credentials:
        input_menu = InputCredentials(
            screen=game_screen, clock=clock, font=font, fps=screen.FPS
        )
        name, email, password = input_menu.input_loop()
        if not name or not email or not password:
            pygame.quit()
            exit()
        else:
            set_credentials(name, email, password)
            auth = AuthPlayer(name=name)
            auth.create_user(email, password)
    else:
        name, email, password = (
            credentials["name"],
            credentials["email"],
            credentials["password"],
        )
        auth = AuthPlayer(name=name)

    auth.login(email, password)

    last_state = state
    selected_role = "orc"
    game = GameData(
        screen=game_screen,
        clock=clock,
        fps=screen.FPS,
        bg_color=colors.GRASS,
        font=font,
        auth=auth,
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
        elif state in [h.lower() for h in heroes.heroes.keys()]:
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
