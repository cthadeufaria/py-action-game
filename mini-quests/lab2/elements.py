from typing import Tuple


# Abstract class for any item in the map
class Element:
    def __init__(self, symbol: str, pos: Tuple[int, int]) -> None:
        self.symbol: str = symbol
        self.x: int = pos[0]
        self.y: int = pos[1]

    def get_pos(self) -> Tuple[int, int]:
        return self.x, self.y

    def set_pos(self, pos: Tuple[int, int]) -> None:
        self.x = pos[0]
        self.y = pos[1]

    def is_adjacent_to(self, el: 'Element') -> bool:
        return True

    def is_overlapping(self, el: 'Element') -> bool:
        return True


# Abstract class for any element that moves
class MovingElement(Element):
    def __init__(self, symbol: str, pos: Tuple[int, int]) -> None:
        super().__init__(symbol, pos)

    def move(self, pos: Tuple[int, int]) -> None:
        self.x = pos[0]
        self.y = pos[1]


# A hero is a moving element controlled by the player
class Hero(MovingElement):
    def __init__(self, symbol: str, pos: Tuple[int, int]) -> None:
        super().__init__(symbol, pos)
        self.has_key: bool = False
        self.has_sword: bool = False


# A dragon is a moving element that moves randomly
class Dragon(MovingElement):
    def __init__(self, symbol: str, pos: Tuple[int, int]):
        super().__init__(symbol, pos)
        self.is_alive: bool = True
