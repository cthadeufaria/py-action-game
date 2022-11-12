"""Any MovingElement that draws health points from a LivingElement."""
from .moving_element import MovingElement


class Projectile(MovingElement):
    """Any MovingElement that draws health points from a LivingElement."""

    def __init__(self) -> None:
        """Initialize Projectile instance."""
        super().__init__()
