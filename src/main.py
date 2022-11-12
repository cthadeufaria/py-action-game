"""Entry point for the game."""

# Standard module imports
import os

# Third-party imports
import pygame

# Local imports
import constants.colors
import constants.screen
import utils.math

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
# TODO: this will be replaced with a function call. Ignore it for now
if __name__ == "__main__":
    game_over = False
    FPS = 30
    while not game_over:
        # Check if user clicks X button in window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        # Add rect to screen for testing purposes
        pygame.draw.rect(
            screen,
            constants.colors.RED,
            pygame.Rect(
                *utils.math.get_center_coordinates(
                    constants.screen.dimensions["medium"], 100, 50
                ),
                100,
                50,
            ),
        )
        pygame.display.flip()

        # Keep a constant FPS rate
        clock.tick(FPS)

    pygame.quit()
