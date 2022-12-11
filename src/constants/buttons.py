"""Constants for controlling properties of buttons in menu screens."""
from typing import Tuple, TypedDict
import constants.colors as colors
from constants.heroes import heroes

menu_type = TypedDict(
    "menu_type",
    {
        "color_text": Tuple[int, int, int],
        "color_light": Tuple[int, int, int],
        "color_dark": Tuple[int, int, int],
        "buttons_spacement": int,
        "button_width": int,
        "button_height": int,
        "options": Tuple[str, ...],
    },
)

menus: dict[str, menu_type] = {
    "main_menu": {
        "color_text": colors.WHITE,
        "color_light": colors.LIGHT_RED,
        "color_dark": colors.RED,
        "buttons_spacement": 20,
        "button_width": 280,
        "button_height": 60,
        "options": ("Play Now", "Options", "Quit"),
    },
    "pause_menu": {
        "color_text": colors.WHITE,
        "color_light": colors.LIGHT_GRAY,
        "color_dark": colors.GRAY,
        "buttons_spacement": 20,
        "button_width": 280,
        "button_height": 60,
        "options": ("Resume", "Options", "Quit"),
    },
    "game_over_menu": {
        "color_text": colors.WHITE,
        "color_light": colors.LIGHT_RED,
        "color_dark": colors.RED,
        "buttons_spacement": 20,
        "button_width": 280,
        "button_height": 60,
        "options": ("Play Again", "Quit"),
    },
    "hero_selection_menu": {
        "color_text": colors.WHITE,
        "color_light": colors.LIGHT_RED,
        "color_dark": colors.RED,
        "buttons_spacement": 20,
        "button_width": 280,
        "button_height": 60,
        "options": tuple(heroes.keys()),
    },
}
