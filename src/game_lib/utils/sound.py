"""Configures the sound utility class for the game."""
from .engine import get_absolute_path
import pygame

pygame.mixer.init()

# Create sound channels
soundtrack_channel = pygame.mixer.Channel(0)
hero_effects_channel = pygame.mixer.Channel(1)
hero_walk_channel = pygame.mixer.Channel(2)
enemy_effects_channel = pygame.mixer.Channel(3)
special_effects_channel = pygame.mixer.Channel(4)


def get_sound_file(file_name: str) -> pygame.mixer.Sound:
    """Retrieve the path of a sound file based on its name."""
    return pygame.mixer.Sound(
        get_absolute_path(__file__, "..", "..", "assets", "sound", file_name)
    )


# Set up sound files
soundtrack = get_sound_file("feupscape.mp3")
projectile = get_sound_file("projectile.mp3")
death_cry = get_sound_file("death_cry.mp3")
mouseover = get_sound_file("mouseover.mp3")


# Adjust volumes
def set_volume(base_volume: float) -> None:
    """Assign a new volume value to all channels."""
    soundtrack_channel.set_volume(base_volume)
    hero_effects_channel.set_volume(base_volume)
    hero_walk_channel.set_volume(base_volume)
    enemy_effects_channel.set_volume(base_volume)
    special_effects_channel.set_volume(base_volume)


def play_soundtrack() -> None:
    """Play game soundtrack."""
    soundtrack_channel.play(soundtrack, loops=-1)  # Repeat forever


def hero_cry() -> None:
    """Play SFX when hero is damaged."""
    hero_effects_channel.play(death_cry)


def play_mouseover() -> None:
    """Play SFX for hovering a menu button."""
    special_effects_channel.play(mouseover)
