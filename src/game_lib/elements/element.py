"""Base class for everything visible on the map."""
import pygame
import sys
from typing import Tuple

sys.path.append("src")
from utils.engine import load_png


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
        self.image_paths = image_paths
        self.dimensions = dimensions
        self.position = position
        self.image_list = []
        for n in image_paths:
            loaded_image, self.rect = load_png(n)
            self.image_list.append(loaded_image)
            self.image_list[-1] = pygame.transform.scale(self.image_list[-1], self.dimensions)
        self.rect.update(self.position, self.dimensions)

    def is_colliding(self, rect: pygame.rect.Rect) -> bool:
        # collision_rect = self.rect.colliderect(any_rect)
        # testing collision with cursor
        point = pygame.mouse.get_pos()
        collision_point = self.rect.collidepoint(point)
        collision_rect = self.rect.colliderect(rect)
        if collision_point or collision_rect:
            print(
                "Collision point " + str(collision_point) + "on " + str(self.position)
            )
            print("Collision rect " + str(collision_rect) + "on " + str(self.position))
            collision = True
        else:
            collision = False
        return collision
