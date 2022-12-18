"""Unit testing for all methods from the Element class."""
from unittest import TestCase
import sys

sys.path.append("..")
from src.game_lib.elements.element import Element
import pygame

pygame.init()
pygame.display.set_mode((2000, 2000), pygame.NOFRAME)


class CheckCollisionMethod(TestCase):
    """Does a simple test to illustrate the capabilities of pytest for the team."""

    def test_overlapping_elements(self):
        """Guarantees that overlapping elements do collide."""
        e1 = Element(
            position=(100, 100), base_image_path="bat.png", dimensions=(50, 30)
        )
        e2 = Element(
            position=(120, 120), base_image_path="ball.png", dimensions=(30, 10)
        )
        self.assertTrue(e1.is_colliding(e2))
        self.assertTrue(e2.is_colliding(e1))

    def test_separated_elements(self):
        """Guarantees that separated elements do not collide."""
        e1 = Element(
            position=(200, 100), base_image_path="bat.png", dimensions=(40, 20)
        )
        e2 = Element(
            position=(100, 50), base_image_path="ball.png", dimensions=(40, 40)
        )
        self.assertFalse(e1.is_colliding(e2))
        self.assertFalse(e2.is_colliding(e1))
