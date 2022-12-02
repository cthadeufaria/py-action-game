"""Constants for controlling static selection screen dimensions."""
from constants.heroes import heroes

# Main menu variables
main_menu = {
    "color": (255, 255, 255),
    "color_light": (170, 170, 170),
    "color_dark": (100, 100, 100),
    # "smallfont": pygame.font.SysFont("Corbel", 35),
    # 'buttons_placement' : (self.screen.width / 2, height / 2),
    "buttons_spacement": 20,
    "button_width": 280,
    "button_height": 60,
    "words": ["Quit", "Play Now", "Options"],
}

# Pause menu variables
pause_menu = {
    "color": (255, 255, 255),
    "color_light": (170, 170, 170),
    "color_dark": (100, 100, 100),
    # "smallfont": pygame.font.SysFont("Corbel", 35),
    # 'buttons_placement' : (self.screen.width / 2, height / 2),
    "buttons_spacement": 20,
    "button_width": 280,
    "button_height": 60,
    "words": ["Quit", "Play Now", "Options"],
}

# Game over screen variables
game_over_menu = {
    "color": (255, 255, 255),
    "color_light": (170, 170, 170),
    "color_dark": (100, 100, 100),
    # "smallfont": pygame.font.SysFont("Corbel", 35),
    # 'buttons_placement' : (self.screen.width / 2, height / 2),
    "buttons_spacement": 20,
    "button_width": 280,
    "button_height": 60,
    "words": ["Quit", "Play Again"],
}

hero_selection_menu = {
    "color": (255, 255, 255),
    "color_light": (170, 170, 170),
    "color_dark": (100, 100, 100),
    # "smallfont": pygame.font.SysFont("Corbel", 35),
    # 'buttons_placement' : (self.screen.width / 2, height / 2),
    "buttons_spacement": 20,
    "button_width": 280,
    "button_height": 60,
    "words": list(heroes.keys()),
}