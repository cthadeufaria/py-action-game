"""Any Element that does not move and can be put in the inventory."""
from .element import Element
from typing import Tuple


class Collectable(Element):
    """Any Element that does not move and can be put in the inventory."""

    def __init__(
        self,
        position: Tuple[int, int],
        image_paths: list[str],
        dimensions: Tuple[int, int],
        heal_value: int,
        rarity: float,
    ) -> None:
        """Initialize Collectable instance."""
        self.rarity = rarity
        self.heal_value = heal_value
        super().__init__(position, image_paths, dimensions)

        if is_colldiding




