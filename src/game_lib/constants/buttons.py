"""Constants for controlling properties of buttons in menu screens."""
from typing import Tuple, TypedDict
from ..constants.colors import WHITE, LIGHT_RED, RED, LIGHT_GRAY, GRAY
from ..constants.heroes import heroes

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
        "color_text": WHITE,
        "color_light": LIGHT_RED,
        "color_dark": RED,
        "buttons_spacement": 20,
        "button_width": 280,
        "button_height": 60,
        "options": ("Play Now", "Options", "Exit"),
    },
    "pause_menu": {
        "color_text": WHITE,
        "color_light": LIGHT_GRAY,
        "color_dark": GRAY,
        "buttons_spacement": 20,
        "button_width": 280,
        "button_height": 60,
        "options": ("Resume", "Options", "Quit"),
    },
    "game_over_menu": {
        "color_text": WHITE,
        "color_light": LIGHT_RED,
        "color_dark": RED,
        "buttons_spacement": 20,
        "button_width": 280,
        "button_height": 60,
        "options": ("Play Again", "Quit"),
    },
    "hero_selection_menu": {
        "color_text": WHITE,
        "color_light": LIGHT_RED,
        "color_dark": RED,
        "buttons_spacement": 20,
        "button_width": 280,
        "button_height": 60,
        "options": tuple(heroes.keys()),
    },
    "options_menu": {
        "color_text": WHITE,
        "color_light": LIGHT_RED,
        "color_dark": RED,
        "buttons_spacement": 20,
        "button_width": 300,
        "button_height": 60,
        "options": ("Volume Up", "Volume Down", "Back", "Quit"),
    },
}
