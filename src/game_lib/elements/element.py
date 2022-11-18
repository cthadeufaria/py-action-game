"""Base class for everything visible on the map."""
import pygame
import sys
from typing import Tuple

sys.path.append("src")
from utils.engine import load_png


class Element(pygame.sprite.Sprite):
    """Base class for everything visible on the map."""

    # question! Is image_paths really a list of strings? If yes: How to pass image_paths as list to self.image?
    # question! Is it advisable to set dimensions through image_paths as in self.dimensions = screen.get_rect()?
    def __init__(
        self,
        position: Tuple[int, int],
        image_paths: list[str],
        dimensions: Tuple[int, int],
    ) -> None:
        """Initialize Element instance."""
        pygame.sprite.Sprite.__init__(self)
        self.image_paths = image_paths
        self.image, self.rect = load_png(image_paths[0])
        self.dimensions = dimensions
        self.image = pygame.transform.scale(self.image, self.dimensions)
        self.position = position
        self.rect.update(self.position, self.dimensions)

    def is_colliding(self, rect: pygame.rect.Rect) -> bool:
        # collision_rect = self.rect.colliderect(any_rect)
        # testing collision with cursor
        point = pygame.mouse.get_pos()
        collision_point = self.rect.collidepoint(point)
        collision_rect = self.rect.colliderect(rect)
        # print("Collision point = " + str(collision_point))
        print("Collision point = " + str(collision_point))
        return collision_rect
