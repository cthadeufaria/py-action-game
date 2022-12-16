"""Auxiliary functions for pygame engine."""
from typing import Tuple
import pygame
import os


def get_absolute_path(file: str, *path_strings: str) -> str:
    """Give the full path a file given its relative path."""
    return os.path.abspath(
        os.path.join(os.path.dirname(os.path.abspath(file)), *path_strings)
    )


def load_png(image_name: str) -> Tuple[pygame.surface.Surface, pygame.rect.Rect]:
    """Load image and return image object."""
    image_path = get_absolute_path(__file__, "..", "..", "assets", "img", image_name)
    try:
        image = pygame.image.load(image_path)
        if image.get_alpha is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except FileNotFoundError:
        print(f"Image not found: {image_path}")
        raise SystemExit
    return image, image.get_rect()
