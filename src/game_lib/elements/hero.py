"""A LivingElement controlled by the player."""
from .living_element import LivingElement


class Hero(LivingElement):
    """A LivingElement controlled by the player."""

    def __init__(self) -> None:
        """Initialize Hero instance."""
        super().__init__()
