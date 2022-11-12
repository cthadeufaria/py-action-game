"""Any Collectable that can be equipped  by the player as a weapon."""
from .collectable import Collectable


class Equipable(Collectable):
    """Any Collectable that can be equipped  by the player as a weapon."""

    def __init__(self) -> None:
        """Initialize Equipable instance."""
        super().__init__()
