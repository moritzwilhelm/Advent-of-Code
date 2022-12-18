#!/usr/bin/env python3
from collections import deque


def parse_input(filename):
    with open(filename) as file:
        return {tuple(map(int, line.split(','))) for line in file}


def get_neighbors(x, y, z):
    for neighbour in (x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1):
        yield neighbour


def part1(data):
    return sum(neighbour not in data for coordinate in data for neighbour in get_neighbors(*coordinate))


def is_in_bounds(lower_bound, upper_bound, x, y, z):
    l_x, l_y, l_z = lower_bound
    u_x, u_y, u_z = upper_bound
    return l_x <= x <= u_x and l_y <= y <= u_y and l_z <= z <= u_z


def part2(data):
    lower_bound = tuple(min(x) - 1 for x in zip(*data))
    upper_bound = tuple(max(x) + 1 for x in zip(*data))

    # flood-fill bounded room and count number of coordinates that are next to a block of lava
    surface_area = 0
    air = deque((lower_bound,))
    visited = set()
    while air:
        for neighbour in get_neighbors(*air.popleft()):
            # ignore coordinate if out of bounded room
            if not is_in_bounds(lower_bound, upper_bound, *neighbour):
                continue

            surface_area += (neighbour in data)
            if neighbour not in data and neighbour not in visited:
                visited.add(neighbour)
                air.append(neighbour)

    return surface_area


if __name__ == '__main__':
    print(f"Part 1: {part1(parse_input('day18.txt'))}")
    print(f"Part 2: {part2(parse_input('day18.txt'))}")
