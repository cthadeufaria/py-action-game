"""Configures the sound utility class for the game."""
from ..utils.engine import get_absolute_path
import pygame

pygame.mixer.init()

# Create sound channels
soundtrack_channel = pygame.mixer.Channel(0)
hero_effects_channel = pygame.mixer.Channel(1)
enemy_effects_channel = pygame.mixer.Channel(2)
special_effects_channel = pygame.mixer.Channel(3)


def get_sound_file(file_name: str) -> pygame.mixer.Sound:
    """Retrieve the path of a sound file based on its name."""
    return pygame.mixer.Sound(
        get_absolute_path(__file__, "..", "..", "assets", "sound", file_name)
    )


# Set up sound files
soundtrack = get_sound_file("feupscape.mp3")
melee_attack = get_sound_file("foom_0.mp3")
ranged_attack = get_sound_file("bow_weapon_shwoop.mp3")
blood_splash = get_sound_file("blood2.mp3")
hero_heal = get_sound_file("instant_heal.mp3")
collect_coin = get_sound_file("collect_coin.mp3")
minotaur_drums = get_sound_file("minotaur_drums.mp3")
room_ambience = get_sound_file("room_ambience.mp3")
# getting_hit = get_sound_file("getting_hit.mp3")
open_menu = get_sound_file("open_menu.mp3")
close_menu = get_sound_file("close_menu.mp3")
mouseover = get_sound_file("mouseover.mp3")
death_cry = get_sound_file("death_cry.mp3")
completed_boss = get_sound_file("completed_boss.mp3")

# Adjust volumes
def volume(base_volume: float) -> None:
    soundtrack_channel.set_volume(base_volume)
    hero_effects_channel.set_volume(base_volume)
    enemy_effects_channel.set_volume(base_volume)
    special_effects_channel.set_volume(base_volume)


# play sound
soundtrack_channel.play(soundtrack, loops=-1)  # Repeat forever


def hero_cry():
    hero_effects_channel.play(death_cry)


# # pause channel
# soundtrack_channel.pause()
#
# # resume channel
# soundtrack_channel.unpause()
#
# # stop channel
# soundtrack_channel.stop()
