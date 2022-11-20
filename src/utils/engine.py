"""Auxiliary functions for pygame engine."""
from typing import Tuple
import pygame
import os


def load_png(image_name: str) -> Tuple[pygame.surface.Surface, pygame.rect.Rect]:
    """Load image and return image object."""
    image_path = os.path.join(
        os.path.split(os.path.dirname(os.path.abspath(__file__)))[0],
        "assets",
        "img",
        image_name,
    )
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
