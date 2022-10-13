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
            ['X' for _ in range(N)],
            *[
                ['X', *[' ' for _ in range(N - 2)], 'X'] for _ in range(N - 2)
            ],
            ['X' for _ in range(N)],
        ]

    # Add walls based on its top_left position, with and height
    def add_walls(self, top_left_pos: Tuple[int, int], width: int, height: int) -> None:
        for line_idx in range(width):
            for col_idx in range(height):
                self.map[top_left_pos[1] + line_idx][top_left_pos[0] + col_idx] = 'X'

    # Add an element to the map based on its position and symbol
    def add_element(self, el: Element) -> None:
        self.map[el.x][el.y] = el.symbol

    # Removes an element from the map based on its position
    def remove_element(self, el: Element) -> None:
        self.map[el.x][el.y] = ' '

    # Returns character in given position
    def get_element(self, pos: Tuple[int, int]) -> str:
        return self.map[pos[0]][pos[1]]

    # Set random position for exit
    def add_exit(self) -> None:
        available_positions = []
        for sq_idx in range(1, self.board_size - 1):

            # Check available places in upper side of the map
            if self.map[1][sq_idx] == ' ':
                available_positions.append((0, sq_idx))

            # Check available places in lower side of the map
            if self.map[self.board_size - 2][sq_idx] == ' ':
                available_positions.append((self.board_size - 1, sq_idx))

            # Check available places in left side of the map
            if self.map[sq_idx][1] == ' ':
                available_positions.append((sq_idx, 0))

            # Check available places in right side of the map
            if self.map[sq_idx][self.board_size - 2] == ' ':
                available_positions.append((sq_idx, self.board_size - 1))

        # Choose random available position and draw exit
        exit_pos = choice(available_positions)
        self.map[exit_pos[0]][exit_pos[1]] = 'E'


class Game:
    def __init__(self, N: int) -> None:
        # Game state
        self.is_over = False
        self.dungeon = Dungeon(N)

        # Initial positions
        self.hero_pos = (1, 1)
        self.key_pos = (N - 2, 1)
        self.dragon_pos = (3, 1)

        # hero state
        self.has_key = False

        # Draw elements' initial positions
        self.dungeon.map[self.hero_pos[0]][self.hero_pos[1]] = 'H'
        self.dungeon.map[self.dragon_pos[0]][self.dragon_pos[1]] = 'D'
        self.dungeon.map[self.key_pos[0]][self.key_pos[1]] = 'K'

    # Display map in the terminal
    def show_map(self) -> None:
        os.system('clear')
        for line in self.dungeon.map:
            print(' '.join(line))
        print('\n')

    # Modify game state when the hero finds a key
    def get_key(self) -> None:
        self.has_key = True
        self.dungeon.map[self.key_pos[0]][self.key_pos[1]] = ' '

    # Main game loop
    def move_hero(self) -> None:
        try:
            x_inc, y_inc = get_direction()
        except InvalidInput:
            self.show_map()
        except ExitGame:
            self.is_over = True

            new_hero_pos = (self.hero.x + x_inc, self.hero.y + y_inc)
            target_square = self.dungeon.get_element(new_hero_pos)

            # Found an empty square
            if target_square == ' ':
                # Erase old pos
                self.dungeon.remove_element(self.hero)

                # Set new pos and draw hero
                self.dungeon. = new_hero_pos
                self.map[self.hero_pos[0]][self.hero_pos[1]] = 'H'
                self.show_map()

                # If there is a dragon nearby, the game is over
                if self.map[self.hero_pos[0] + 1][self.hero_pos[1]] == 'D' or \
                        self.map[self.hero_pos[0] - 1][self.hero_pos[1]] == 'D' or \
                        self.map[self.hero_pos[0]][self.hero_pos[1] + 1] == 'D' or \
                        self.map[self.hero_pos[0]][self.hero_pos[1] - 1] == 'D':
                    print('\nThe dragon killed you!\n')
                    self.is_over = True

            # Found the key
            elif target_square == 'K':
                self.get_key()

                # Erase old position
                self.map[self.hero_pos[0]][self.hero_pos[1]] = ' '

                # Set new pos and draw hero
                self.hero_pos = new_hero_pos
                self.map[self.hero_pos[0]][self.hero_pos[1]] = 'H'
                self.show_map()

            # Found the exit
            elif target_square == 'E':
                if self.has_key:
                    self.is_over = True
                    print('\nYou found the exit!\n')
                else:
                    self.show_map()

            # Invalid movement
            else:
                self.show_map()


if __name__ == '__main__':
    # Init game with size 10 and add hard-coded walls
    game_instance = Game(10)
    game_instance.add_walls((2, 2), 3, 2)
    game_instance.add_walls((2, 6), 3, 2)
    game_instance.add_walls((5, 2), 3, 1)
    game_instance.add_walls((5, 6), 2, 1)
    game_instance.add_walls((7, 2), 6, 1)
    game_instance.add_exit()
    game_instance.show_map()

    hero = Hero(symbol='🧔', pos=(4, 4))
    dragon = Dragon(symbol='🐉', pos=(4, 4))
    key = Element(symbol='🗡️', pos=(4, 4))

    while not game_instance.is_over:
        game_instance.move_hero()
