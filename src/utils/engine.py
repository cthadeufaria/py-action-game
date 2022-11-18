"""Auxiliary functions for pygame engine."""
from typing import Tuple
import pygame
import os


def load_png(name: str) -> Tuple[pygame.surface.Surface, pygame.rect.Rect]:
    """Load image and return image object."""
    fullname = os.path.join("src/assets/img", name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except FileNotFoundError:
        print(f"Cannot load image: {fullname}")
        raise SystemExit
    return image, image.get_rect()
