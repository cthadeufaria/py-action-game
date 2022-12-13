import os
from typing import Tuple
from random import choice
from elements import Element, Hero, Dragon
from user_input import get_direction, ExitGame, InvalidInput


class Dungeon:
    def __init__(self, N: int) -> None:
        self.board_size = N

        # Create map frame with blank interior
        self.map = [
            ["X" for _ in range(N)],
            *[["X", *[" " for _ in range(N - 2)], "X"] for _ in range(N - 2)],
            ["X" for _ in range(N)],
        ]

    # Add walls based on its top_left position, with and height
    def add_walls(self, top_left_pos: Tuple[int, int], width: int, height: int) -> None:
        for line_idx in range(width):
            for col_idx in range(height):
                self.map[top_left_pos[1] + line_idx][top_left_pos[0] + col_idx] = "X"

    # Add an element to the map based on its position and symbol
    def add_element(self, el: Element) -> None:
        self.map[el.x][el.y] = el.symbol

    # Removes an element from the map based on its position
    def remove_element(self, el: Element) -> None:
        self.map[el.x][el.y] = " "

    # Returns character in given position
    def get_element(self, pos: Tuple[int, int]) -> str:
        return self.map[pos[0]][pos[1]]

    # Set random position for exit
    def add_exit(self) -> None:
        available_positions = []
        for sq_idx in range(1, self.board_size - 1):

            # Check available places in upper side of the map
            if self.map[1][sq_idx] == " ":
                available_positions.append((0, sq_idx))

            # Check available places in lower side of the map
            if self.map[self.board_size - 2][sq_idx] == " ":
                available_positions.append((self.board_size - 1, sq_idx))

            # Check available places in left side of the map
            if self.map[sq_idx][1] == " ":
                available_positions.append((sq_idx, 0))

            # Check available places in right side of the map
            if self.map[sq_idx][self.board_size - 2] == " ":
                available_positions.append((sq_idx, self.board_size - 1))

        # Choose random available position and draw exit
        exit_pos = choice(available_positions)
        self.map[exit_pos[0]][exit_pos[1]] = "E"

    # Display map in the terminal
    def show_map(self) -> None:
        os.system("clear")
        for line in self.map:
            print(" ".join(line))
        print("\n")


if __name__ == "__main__":
    # Init game with size 10 and add hard-coded walls
    dungeon = Dungeon(10)
    dungeon.add_walls((2, 2), 3, 2)
    dungeon.add_walls((2, 6), 3, 2)
    dungeon.add_walls((5, 2), 3, 1)
    dungeon.add_walls((5, 6), 2, 1)
    dungeon.add_walls((7, 2), 6, 1)
    dungeon.add_exit()
    dungeon.show_map()

    hero = Hero(symbol="H", pos=(4, 5))
    dragon = Dragon(symbol="D", pos=(1, 1))
    sword = Element(symbol="S", pos=(4, 4))
    dungeon_exit = Element(symbol="E", pos=(0, 0))

    # Add elements to dungeon
    [dungeon.add_element(x) for x in [hero, dragon, sword, dungeon_exit]]

    is_over = False
    while not is_over:
        try:
            x_inc, y_inc = get_direction()

            new_hero_pos = (hero.x + x_inc, hero.y + y_inc)
            target_square = dungeon.get_element(new_hero_pos)

            # Found an empty square
            if target_square == " ":
                # Erase old pos
                dungeon.remove_element(hero)

                # Set new pos and draw hero
                hero.set_pos(new_hero_pos)
                dungeon.add_element(hero)

                # If there is a dragon nearby, the game is over
                if hero.is_adjacent_to(dragon):
                    print("\nThe dragon killed you!\n")
                    is_over = True

                # Display updated map
                else:
                    dungeon.show_map()

            # Found the sword
            elif hero.is_overlapping(sword):
                dungeon.remove_element(sword)
                hero.has_sword = True
                dungeon.add_element(hero)
                dungeon.show_map()

            # Found the exit
            elif hero.is_overlapping(dungeon_exit):
                if hero.has_sword:
                    is_over = True
                    print("\nYou found the exit!\n")
                else:
                    dungeon.show_map()

            # Invalid movement
            else:
                dungeon.show_map()

        except InvalidInput:
            dungeon.show_map()

        except ExitGame:
            is_over = True
