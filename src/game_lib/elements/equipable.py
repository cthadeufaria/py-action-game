"""Any Collectable that can be equipped  by the player as a weapon."""
from .collectable import Collectable


class Equipable(Collectable):
    """Any Collectable that can be equipped  by the player as a weapon."""

    def __init__(self, attack_force: int, weight: float) -> None:
        self.attack_force = attack_force
        self.weight = weight
        """Initialize Equipable instance."""
        super().__init__()
