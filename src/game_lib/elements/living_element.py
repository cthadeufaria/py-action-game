"""Any MovingElement that has health points."""
from .moving_element import MovingElement


class LivingElement(MovingElement):
    """Any MovingElement that has health points."""

    def __init__(self) -> None:
        """Initialize LivingElement instance."""
        super().__init__()
