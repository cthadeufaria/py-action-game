"""Any Element that does not move and can be put in the inventory."""
from .element import Element


class Collectable(Element):
    """Any Element that does not move and can be put in the inventory."""

    def __init__(self) -> None:
        """Initialize Collectable instance."""
        super().__init__()
