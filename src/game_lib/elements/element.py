"""Base class for everything visible on the map."""
import pygame
from typing import Tuple
from ..utils.engine import load_png


class Element(pygame.sprite.Sprite):
    """Base class for everything visible on the map."""

    def __init__(
        self,
        position: Tuple[int, int],
        image_paths: list[str],
        dimensions: Tuple[int, int],
    ) -> None:
        """Initialize Element instance."""
        pygame.sprite.Sprite.__init__(self)
        self.rect: pygame.rect.Rect
        self.image: pygame.surface.Surface
        self.image_paths = image_paths
        self.dimensions = dimensions
        self.position = position
        self.image_list = []
        for n in image_paths:
            loaded_image, self.rect = load_png(n)
            self.image_list.append(loaded_image)
            self.image_list[-1] = pygame.transform.scale(
                self.image_list[-1], self.dimensions
            )
        self.image = self.image_list[0]
        self.rect.update(self.position, self.dimensions)

    def is_colliding(self, elem: "Element") -> bool:
        """Check if element is colliding with another element."""
        return self.rect.colliderect(elem.rect)

    # TODO: unit testing for colliding method
