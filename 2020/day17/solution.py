#!/usr/bin/env python3


def parse_input():
    active_cubes = set()
    with open('input') as file:
        for x, line in enumerate(file):
            for y, c in enumerate(line):
                if c == '#':
                    active_cubes.add((x, y, 0))
    return active_cubes


def part1(active_cubes):
    cubes = active_cubes.copy()
    for _ in range(6):
        new_cubes = set()
        for x in range(min(cube[0] for cube in cubes) - 1, max(cube[0] for cube in cubes) + 2):
            for y in range(min(cube[1] for cube in cubes) - 1, max(cube[1] for cube in cubes) + 2):
                for z in range(min(cube[2] for cube in cubes) - 1, max(cube[2] for cube in cubes) + 2):
                    current_cube = (x, y, z)
                    active_neighbors = 0
                    for x_off in [-1, 0, 1]:
                        for y_off in [-1, 0, 1]:
                            for z_off in [-1, 0, 1]:
                                neighbor = (x + x_off, y + y_off, z + z_off)
                                if neighbor != current_cube and neighbor in cubes:
                                    active_neighbors += 1
                    if current_cube in cubes and 1 < active_neighbors < 4 or current_cube not in cubes and active_neighbors == 3:
                        new_cubes.add(current_cube)
        cubes = new_cubes
    return len(cubes)


def part2(active_cubes):
    cubes = {(cube[0], cube[1], cube[2], 0) for cube in active_cubes}
    for _ in range(6):
        new_cubes = set()
        for x in range(min(cube[0] for cube in cubes) - 1, max(cube[0] for cube in cubes) + 2):
            for y in range(min(cube[1] for cube in cubes) - 1, max(cube[1] for cube in cubes) + 2):
                for z in range(min(cube[2] for cube in cubes) - 1, max(cube[2] for cube in cubes) + 2):
                    for w in range(min(cube[3] for cube in cubes) - 1, max(cube[3] for cube in cubes) + 2):
                        current_cube = (x, y, z, w)
                        active_neighbors = 0
                        for x_off in [-1, 0, 1]:
                            for y_off in [-1, 0, 1]:
                                for z_off in [-1, 0, 1]:
                                    for w_off in [-1, 0, 1]:
                                        neighbor = (x + x_off, y + y_off, z + z_off, w + w_off)
                                        if neighbor != current_cube and neighbor in cubes:
                                            active_neighbors += 1
                        if current_cube in cubes and 1 < active_neighbors < 4 or current_cube not in cubes and active_neighbors == 3:
                            new_cubes.add(current_cube)
        cubes = new_cubes
    return len(cubes)


def main():
    active_cubes = parse_input()
    print("Part 1:", part1(active_cubes))
    print("Part 2:", part2(active_cubes))


if __name__ == '__main__':
    main()
