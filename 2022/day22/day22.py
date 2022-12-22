#!/usr/bin/env python3
import re
from functools import cache


def parse_input(filename):
    board = set()
    walls = set()
    with open(filename) as file:
        serialized_board, serialized_path = file.read().split('\n\n')

    for row, line in enumerate(serialized_board.splitlines()):
        for column, c in enumerate(line):
            if c == '.':
                board.add((column, row))
            elif c == '#':
                board.add((column, row))
                walls.add((column, row))
    return board, walls, tuple(re.findall("[0-9]+|[LR]", serialized_path.strip()))


def calculate_password(data, is_cube=False):
    board, walls, path = data
    current_position = (50, 0)
    current_direction = 0  # RIGHT = 0, DOWN = 1, LEFT = 2, UP = 3

    @cache
    def get_column_bounds(row):
        return min(c for c, r in board if r == row), max(c for c, r in board if r == row)

    @cache
    def get_row_bounds(column):
        return min(r for c, r in board if c == column), max(r for c, r in board if c == column)

    def perform_move_on_grid(column, row, direction):
        min_column, max_column = get_column_bounds(row)
        min_row, max_row = get_row_bounds(column)
        if direction == 0:
            new_column = column + 1 if column + 1 <= max_column else min_column
            new_row = row
        elif direction == 1:
            new_column = column
            new_row = row + 1 if row + 1 <= max_row else min_row
        elif direction == 2:
            new_column = column - 1 if column - 1 >= min_column else max_column
            new_row = row
        else:
            new_column = column
            new_row = row - 1 if row - 1 >= min_row else max_row

        if (new_column, new_row) in walls:
            return (column, row), direction

        return (new_column, new_row), direction

    def determine_cube(column, row):
        return column // 50, row // 50

    def perform_move_on_cube(column, row, direction):
        cube = determine_cube(column, row)
        # new_cube = None
        if direction == 0:
            if (column + 1, row) not in board:
                if cube == (0, 3):
                    new_column = 50 + (row - 150)
                    new_row = 149
                    new_direction = 3
                    # new_cube = (1, 2)
                elif cube == (1, 2):
                    new_column = 149
                    new_row = 49 - (row - 100)
                    new_direction = 2
                    # new_cube = (2, 0)
                elif cube == (1, 1):
                    new_column = 100 + (row - 50)
                    new_row = 49
                    new_direction = 3
                    # new_cube = (2, 0)
                elif cube == (2, 0):
                    new_column = 99
                    new_row = 149 - row
                    new_direction = 2
                    # new_cube = (1, 2)
            else:
                new_column = column + 1
                new_row = row
                new_direction = direction
        elif direction == 1:
            if (column, row + 1) not in board:
                if cube == (0, 3):
                    new_column = 100 + column
                    new_row = 0
                    new_direction = 1
                    # new_cube = (2, 0)
                elif cube == (1, 2):
                    new_column = 49
                    new_row = 150 + (column - 50)
                    new_direction = 2
                    # new_cube = (0, 3)
                elif cube == (2, 0):
                    new_column = 99
                    new_row = 50 + (column - 100)
                    new_direction = 2
                    # new_cube = (1, 1)
            else:
                new_column = column
                new_row = row + 1
                new_direction = direction
        elif direction == 2:
            if (column - 1, row) not in board:
                if cube == (0, 3):
                    new_column = 50 + (row - 150)
                    new_row = 0
                    new_direction = 1
                    # new_cube = (1, 0)
                elif cube == (0, 2):
                    new_column = 50
                    new_row = 49 - (row - 100)
                    new_direction = 0
                    # new_cube = (1, 0)
                elif cube == (1, 1):
                    new_column = row - 50
                    new_row = 100
                    new_direction = 1
                    # new_cube = (0, 2)
                elif cube == (1, 0):
                    new_column = 0
                    new_row = 149 - row
                    new_direction = 0
                    # new_cube = (0, 2)
            else:
                new_column = column - 1
                new_row = row
                new_direction = direction
        else:
            if (column, row - 1) not in board:
                if cube == (0, 2):
                    new_column = 50
                    new_row = 50 + column
                    new_direction = 0
                    # new_cube = (1, 1)
                elif cube == (1, 0):
                    new_column = 0
                    new_row = 150 + (column - 50)
                    new_direction = 0
                    # new_cube = (0, 3)
                elif cube == (2, 0):
                    new_column = column - 100
                    new_row = 199
                    new_direction = 3
                    # new_cube = (0, 3)
            else:
                new_column = column
                new_row = row - 1
                new_direction = direction

        if (new_column, new_row) in walls:
            return (column, row), direction  # , None

        return (new_column, new_row), new_direction  # , new_cube

    move_function = perform_move_on_cube if is_cube else perform_move_on_grid

    for action in path:
        if action == 'R':
            current_direction += 1
            current_direction %= 4
        elif action == 'L':
            current_direction -= 1
            current_direction %= 4
        else:
            for _ in range(int(action)):
                new_position, new_direction = move_function(*current_position, current_direction)
                if new_position == current_position:
                    assert current_direction == new_direction
                    break
                current_position, current_direction = new_position, new_direction

    return (current_position[1] + 1) * 1000 + (current_position[0] + 1) * 4 + current_direction


def part1(data):
    return calculate_password(data)


def part2(data):
    return calculate_password(data, is_cube=True)


if __name__ == '__main__':
    print(f"Part 1: {part1(parse_input('day22.txt'))}")
    print(f"Part 2: {part2(parse_input('day22.txt'))}")
