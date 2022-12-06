from unittest import TestCase
import sys
sys.path.append('..')
from src.game_lib.elements.element import Element
import pygame
pygame.init()
pygame.display.set_mode((2000, 2000), pygame.NOFRAME)


class CheckCollisionMethod(TestCase):
    def test_overlapping_elements(self):
        e1 = Element(position=(100, 100), image_paths=['bat.png'], dimensions=(50, 30))
        e2 = Element(position=(120, 120), image_paths=['ball.png'], dimensions=(30, 10))
        self.assertTrue(e1.is_colliding(e2))
        self.assertTrue(e2.is_colliding(e1))

    def test_separated_elements(self):
        e1 = Element(position=(200, 100), image_paths=['bat.png'], dimensions=(40, 20))
        e2 = Element(position=(100,  50), image_paths=['ball.png'], dimensions=(40, 40))
        self.assertFalse(e1.is_colliding(e2))
        self.assertFalse(e2.is_colliding(e1))
