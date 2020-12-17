#!/usr/bin/env python3
from collections import defaultdict


def parse_input():
    active_cubes = set()
    with open('input') as file:
        for x, line in enumerate(file):
            for y, c in enumerate(line):
                if c == '#':
                    active_cubes.add((x, y))
    return active_cubes


def part1(active_cubes):
    cubes = {(cube[0], cube[1], 0) for cube in active_cubes}
    for _ in range(6):
        active_neighbors = defaultdict(int)
        for x, y, z in cubes:
            for x_off in [-1, 0, 1]:
                for y_off in [-1, 0, 1]:
                    for z_off in [-1, 0, 1]:
                        neighbor = (x + x_off, y + y_off, z + z_off)
                        if neighbor != (x, y, z):
                            active_neighbors[neighbor] += 1
        new_cubes = set()
        for cube in active_neighbors:
            if cube in cubes and 1 < active_neighbors[cube] < 4 or cube not in cubes and active_neighbors[cube] == 3:
                new_cubes.add(cube)
        cubes = new_cubes
    return len(cubes)


def part2(active_cubes):
    cubes = {(cube[0], cube[1], 0, 0) for cube in active_cubes}
    for _ in range(6):
        active_neighbors = defaultdict(int)
        for x, y, z, w in cubes:
            for x_off in [-1, 0, 1]:
                for y_off in [-1, 0, 1]:
                    for z_off in [-1, 0, 1]:
                        for w_off in [-1, 0, 1]:
                            neighbor = (x + x_off, y + y_off, z + z_off, w + w_off)
                            if neighbor != (x, y, z, w):
                                active_neighbors[neighbor] += 1
        new_cubes = set()
        for cube in active_neighbors:
            if cube in cubes and 1 < active_neighbors[cube] < 4 or cube not in cubes and active_neighbors[cube] == 3:
                new_cubes.add(cube)
        cubes = new_cubes
    return len(cubes)


def main():
    active_cubes = parse_input()
    print("Part 1:", part1(active_cubes))
    print("Part 2:", part2(active_cubes))


if __name__ == '__main__':
    main()
