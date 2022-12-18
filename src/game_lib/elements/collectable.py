"""Any Element that does not move and can be put in the inventory."""
from .element import Element
from typing import Tuple


class Collectable(Element):
    """Any Element that does not move and can be put in the inventory."""

    def __init__(
        self,
        position: Tuple[int, int],
        base_image_path: str,
        dimensions: Tuple[int, int],
        rarity: float,
    ) -> None:
        """Initialize Collectable instance."""
        self.rarity = rarity
        super().__init__(position, base_image_path, dimensions)
