#!/usr/bin/env python3
from collections import defaultdict
from itertools import product
from operator import add


def parse_input():
    active_cubes = set()
    with open('input') as file:
        for x, line in enumerate(file):
            for y, c in enumerate(line):
                if c == '#':
                    active_cubes.add((x, y))
    return active_cubes


def get_neighbors(cube):
    return [tuple(map(add, cube, offset)) for offset in product(range(-1, 2), repeat=len(cube)) if any(offset)]


def simulate_rounds(cubes, rounds=6):
    for _ in range(rounds):
        active_neighbors = defaultdict(int)
        for cube in cubes:
            for neighbor in get_neighbors(cube):
                active_neighbors[neighbor] += 1
        new_cubes = set()
        for cube in active_neighbors:
            if cube in cubes and 1 < active_neighbors[cube] < 4 or cube not in cubes and active_neighbors[cube] == 3:
                new_cubes.add(cube)
        cubes = new_cubes
    return len(cubes)


def part1(active_cubes):
    cubes = {(cube[0], cube[1], 0) for cube in active_cubes}
    return simulate_rounds(cubes)


def part2(active_cubes):
    cubes = {(cube[0], cube[1], 0, 0) for cube in active_cubes}
    return simulate_rounds(cubes)


def main():
    active_cubes = parse_input()
    print("Part 1:", part1(active_cubes))
    print("Part 2:", part2(active_cubes))


if __name__ == '__main__':
    main()
