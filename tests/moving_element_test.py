from unittest import TestCase
import sys
sys.path.append('..')
from src.game_lib.elements.moving_element import MovingElement
import pygame
pygame.init()
pygame.display.set_mode((2000, 2000), pygame.NOFRAME)


class CheckMovingMethod(TestCase):
    def test_flying_and_colliding(self):
        pass

    def test_flying_and_not_colliding(self):
        pass

    def test_not_flying_and_colliding(self):
        pass

    def test_not_flying_and_not_colliding(self):
        pass
