"""Any Element that can move on the game map."""
from .element import Element


class MovingElement(Element):
    """Any Element that can move on the game map."""

    def __init__(self) -> None:
        """Initialize MovingElement instance."""
        super().__init__()
