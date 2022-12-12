#!/usr/bin/env python3
from collections import deque
from math import inf


def parse_input(filename):
    with open(filename) as file:
        return [line.strip() for line in file]


def is_valid_neighbor(data, x, y, neighbour_x, neighbour_y):
    if 0 <= neighbour_x < len(data) and 0 <= neighbour_y < len(data[0]):
        if ord('a') <= ord(data[neighbour_x][neighbour_y]) <= ord(data[x][y]) + 1:
            return True
        elif data[x][y] == 'S' and data[neighbour_x][neighbour_y] in {'a', 'b'}:
            return True
        elif data[x][y] in {'y', 'z'} and data[neighbour_x][neighbour_y] in {'z', 'E'}:
            return True

    return False


def shortest_hike(data, start):
    position = (start, 0)
    seen = {start}
    window = deque((position,))
    while window:
        (x, y), depth = window.popleft()
        if data[x][y] == 'E':
            return depth
        for neighbour in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
            if neighbour not in seen and is_valid_neighbor(data, x, y, *neighbour):
                seen.add(neighbour)
                window.append((neighbour, depth + 1))

    return inf


def part1(data):
    return shortest_hike(data, (0, 0))


def part2(data):
    return min(
        shortest_hike(data, (x, y)) for x in range(len(data)) for y in range(len(data[0])) if data[x][y] in {'a', 'S'})


if __name__ == '__main__':
    print(f"Part 1: {part1(parse_input('day12.txt'))}")
    print(f"Part 2: {part2(parse_input('day12.txt'))}")
