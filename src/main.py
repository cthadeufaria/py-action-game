"""Entry point for the game."""

# Standard module imports
import os

# Third-party imports
import pygame

# Local imports
import constants.colors
import constants.screen
from game_lib.environment.game_data import GameData

# Center window
os.environ["SDL_VIDEO_CENTERED"] = "1"

# Initialize game engine
pygame.init()

# Set window name, size and default font
pygame.display.set_caption("FEUPscape")
screen = pygame.display.set_mode(constants.screen.dimensions["medium"])
font = pygame.font.Font("assets/wonder.ttf", 25)

# Create clock for game loop
clock = pygame.time.Clock()

# Entry point, game loop
if __name__ == "__main__":
    game = GameData(
        screen=screen,
        clock=clock,
        fps=constants.screen.FPS,
        bg_color=constants.colors.GRASS,
        font=font,
    )
    game.game_loop()
