"""Unit testing for all methods from the MovingElement class."""
from unittest import TestCase
import sys

sys.path.append("..")
from src.game_lib.elements.moving_element import Element
from src.game_lib.elements.moving_element import MovingElement
import pygame

pygame.init()
pygame.display.set_mode((2000, 2000), pygame.NOFRAME)

top_wall = Element(position=(0, 0), base_image_path="ball.png", dimensions=(100, 20))
right_wall = Element(position=(80, 0), base_image_path="ball.png", dimensions=(20, 100))
bottom_wall = Element(position=(0, 80), base_image_path="ball.png", dimensions=(100, 20))
left_wall = Element(position=(0, 0), base_image_path="ball.png", dimensions=(20, 100))

collision_paths = {
    "top": {"velocity": (0, -1), "wall": top_wall},
    "right": {"velocity": (1, 0), "wall": right_wall},
    "bottom": {"velocity": (0, 1), "wall": bottom_wall},
    "left": {"velocity": (-1, 0), "wall": left_wall},
}


class CheckMovingMethod(TestCase):
    """Check if the move method respects walls and adjusts each element's position."""

    def test_flying_and_colliding(self):
        """Guarantees that a flying element trying to collide with a wall
        is over the wall after the function."""
        for path in collision_paths:
            flying_element = MovingElement(
                (45, 45),
                base_image_path="bat.png",
                dimensions=(10, 10),
                base_speed=40,
                can_fly=True,
            )
            flying_element.velocity = collision_paths[path]["velocity"]
            flying_element.move([collision_paths[path]["wall"].rect])
            self.assertTrue(flying_element.is_colliding(collision_paths[path]["wall"]))

    def test_flying_and_not_colliding(self):
        """Guarantees that a flying element trying to move outside a wall
        is not over the wall after the function."""
        for path in collision_paths:
            flying_element = MovingElement(
                (45, 45),
                base_image_path="bat.png",
                dimensions=(10, 10),
                base_speed=25,
                can_fly=True,
            )
            flying_element.velocity = collision_paths[path]["velocity"]
            flying_element.move([collision_paths[path]["wall"].rect])
            self.assertFalse(flying_element.is_colliding(collision_paths[path]["wall"]))

    def test_not_flying_and_colliding(self):
        """Guarantees that a non-flying element trying to collide with a wall
        is put outside the wall after the function."""
        for path in collision_paths:
            non_flying_element = MovingElement(
                (45, 45),
                base_image_path="bat.png",
                dimensions=(10, 10),
                base_speed=40,
                can_fly=False,
            )
            non_flying_element.velocity = collision_paths[path]["velocity"]
            non_flying_element.move([collision_paths[path]["wall"].rect])
            self.assertFalse(
                non_flying_element.is_colliding(collision_paths[path]["wall"])
            )

    def test_not_flying_and_not_colliding(self):
        """Guarantees that a non-flying element trying to move outside a wall
        is not over the wall after the function."""
        for path in collision_paths:
            non_flying_element = MovingElement(
                (45, 45),
                base_image_path="bat.png",
                dimensions=(10, 10),
                base_speed=25,
                can_fly=False,
            )
            non_flying_element.velocity = collision_paths[path]["velocity"]
            non_flying_element.move([collision_paths[path]["wall"].rect])
            self.assertFalse(
                non_flying_element.is_colliding(collision_paths[path]["wall"])
            )
