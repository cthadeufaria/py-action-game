"""Base class for everything visible on the map."""
import pygame
from typing import Tuple
from ..utils.engine import load_png


class Element(pygame.sprite.Sprite):
    """Base class for everything visible on the map."""

    def __init__(
        self,
        position: Tuple[int, int],
        base_image_path: str,
        dimensions: Tuple[int, int],
    ) -> None:
        """Initialize Element instance."""
        pygame.sprite.Sprite.__init__(self)
        self.rect: pygame.rect.Rect
        self.image: pygame.surface.Surface
        self.dimensions = dimensions
        self.position = position
        loaded_image, self.rect = load_png(base_image_path)
        self.image = pygame.transform.scale(loaded_image, self.dimensions)
        self.rect.update(self.position, self.dimensions)

    def is_colliding(self, elem: "Element") -> bool:
        """Check if element is colliding with another element."""
        return self.rect.colliderect(elem.rect)
