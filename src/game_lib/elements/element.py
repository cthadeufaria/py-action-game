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

    def is_colliding(self, any_rect: pygame.Rect) -> bool:
        collision_rect = self.rect.colliderect(any_rect)
        # testing collision with cursor
        point = pygame.mouse.get_pos()
        collision_point = self.rect.collidepoint(point)
        if collision_point:
            self.rect.update((320, 320), (320, 320))
        return collision_rect


def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Basic Pong")

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    # Initialise Element
    element = Element((320, 320), ["ball.png"], (128, 128))

    # Initialise sprites
    elementsprite = pygame.sprite.RenderPlain(element)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Initialise clock
    clock = pygame.time.Clock()

    # Event loop
    while True:
        # Make sure game doesn't run at more than 60 frames per second
        clock.tick(60)

        screen.blit(background, element.rect, element.rect)
        elementsprite.update()
        elementsprite.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
