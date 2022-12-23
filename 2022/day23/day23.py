#!/usr/bin/env python3
from collections import deque, Counter

DIRECTIONS = deque((((-1, -1), (0, -1), (1, -1)),  # NW, N, NE
                    ((-1, 1), (0, 1), (1, 1)),  # SW, S, SE
                    ((-1, 1), (-1, 0), (-1, -1)),  # NW, W, SW
                    ((1, 1), (1, 0), (1, -1))))  # NE, E, SE


def parse_input(filename):
    with open(filename) as file:
        return [(column, row) for row, line in enumerate(file) for column, c in enumerate(line) if c == '#']


def print_elves(elves):
    for y in range(min(j for _, j in elves), max(j for _, j in elves) + 1):
        for x in range(min(i for i, _ in elves), max(i for i, _ in elves) + 1):
            if (x, y) not in elves:
                print('.', end='')
            else:
                print('#', end='')
        print()


def count_empty_ground_tiles(elves):
    return (max(j for _, j in elves) - min(j for _, j in elves) + 1) \
        * (max(i for i, _ in elves) - min(i for i, _ in elves) + 1) - len(elves)


def has_to_move(blocked, x, y):
    for i, j in (x - 1, y + 1), (x, y + 1), (x + 1, y + 1), (x - 1, y), (x + 1, y), (x - 1, y - 1), (x, y - 1), (
            x + 1, y - 1):
        if (i, j) in blocked:
            return True
    return False


def update_elf_position(elves, x, y):
    for (dx1, dy1), (dx2, dy2), (dx3, dy3) in DIRECTIONS:
        if (x + dx1, y + dy1) not in elves and (x + dx2, y + dy2) not in elves and (x + dx3, y + dy3) not in elves:
            return x + dx2, y + dy2

    return x, y


def simulate(elves, limit=None):
    rounds = 0
    while True:
        # determine elf movements
        elf_movements = {}
        for x, y in elves:
            if has_to_move(elves, x, y):
                elf_movements[(x, y)] = update_elf_position(elves, x, y)
            else:
                elf_movements[(x, y)] = (x, y)

        # check for collisions
        position_collisions = Counter(elf_movements.values())
        for x, y in elves:
            if position_collisions[elf_movements[(x, y)]] > 1:
                elf_movements[(x, y)] = (x, y)

        # check termination condition
        if elves == set(elf_movements.values()) or rounds == limit:
            # reset DIRECTIONS
            DIRECTIONS.rotate(rounds)
            return elves, rounds + 1

        # update elf positions
        elves = set(elf_movements.values())

        DIRECTIONS.rotate(-1)
        rounds += 1


def part1(data):
    elves, _ = simulate(data, 10)
    return count_empty_ground_tiles(elves)


def part2(data):
    _, rounds = simulate(data)
    return rounds


if __name__ == '__main__':
    print(f"Part 1: {part1(parse_input('day23.txt'))}")
    print(f"Part 2: {part2(parse_input('day23.txt'))}")
