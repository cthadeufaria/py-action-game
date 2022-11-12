"""Any LivingElement that can attack and be attacked by a Hero."""
from .living_element import LivingElement


class Enemy(LivingElement):
    """Any LivingElement that can attack and be attacked by a Hero."""

    def __init__(self) -> None:
        """Initialize Enemy instance."""
        super().__init__()
