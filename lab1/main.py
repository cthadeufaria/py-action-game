import os
from typing import Tuple
from random import choice


class Game:
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

        # Game state
        self.is_over = False

        # Initial positions
        self.hero_pos = (1, 1)
        self.key_pos = (N - 2, 1)
        self.dragon_pos = (3, 1)

        # hero state
        self.has_key = False

        # Draw elements' initial positions
        self.map[self.hero_pos[0]][self.hero_pos[1]] = 'H'
        self.map[self.dragon_pos[0]][self.dragon_pos[1]] = 'D'
        self.map[self.key_pos[0]][self.key_pos[1]] = 'K'

    # Add walls based on its top_left position, with and height
    def add_walls(self, top_left_pos: Tuple[int, int], width: int, height: int) -> None:
        for line_idx in range(width):
            for col_idx in range(height):
                self.map[top_left_pos[1] + line_idx][top_left_pos[0] + col_idx] = 'X'

    # Set random position for exit
    def add_exit(self):
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

    # Display map in the terminal
    def show_map(self) -> None:
        os.system('clear')
        for line in self.map:
            print(' '.join(line))
        print('\n')

    # Modify game state when the hero finds a key
    def get_key(self) -> None:
        self.has_key = True
        self.map[self.key_pos[0]][self.key_pos[1]] = ' '

    # Main game loop
    def move_hero(self) -> None:
        # Get pressed key
        direction = input('Where to move? [WASD] (X to exit) ').upper()

        # If exit key was pressed, quit the game
        if direction == 'X':
            self.is_over = True

        # Invalid key: clear the console and ask again
        if direction not in ['W', 'A', 'S', 'D']:
            self.show_map()

        # Valid key
        else:
            new_hero_pos = []

            # Determine new position
            if direction == 'W':
                new_hero_pos = (self.hero_pos[0] - 1, self.hero_pos[1])
            if direction == 'A':
                new_hero_pos = (self.hero_pos[0], self.hero_pos[1] - 1)
            if direction == 'S':
                new_hero_pos = (self.hero_pos[0] + 1, self.hero_pos[1])
            if direction == 'D':
                new_hero_pos = (self.hero_pos[0], self.hero_pos[1] + 1)

            target_square = self.map[new_hero_pos[0]][new_hero_pos[1]]

            # Found an empty square
            if target_square == ' ':
                # Erase old pos
                self.map[self.hero_pos[0]][self.hero_pos[1]] = ' '

                # Set new pos and draw hero
                self.hero_pos = new_hero_pos
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

    while not game_instance.is_over:
        game_instance.move_hero()
