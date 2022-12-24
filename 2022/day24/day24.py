#!/usr/bin/env python3
from collections import deque
from functools import cache
from math import lcm


def parse_input(filename):
    valley = set()
    blizzards = set()
    with open(filename) as file:
        for row, line in enumerate(file, start=-1):
            for column, field in enumerate(line.strip(), start=-1):
                if field != '#':
                    if field == '>':
                        blizzards.add(((column, row), (1, 0)))
                    elif field == '<':
                        blizzards.add(((column, row), (-1, 0)))
                    elif field == '^':
                        blizzards.add(((column, row), (0, -1)))
                    elif field == 'v':
                        blizzards.add(((column, row), (0, 1)))
                    valley.add((column, row))

    return valley, blizzards, max(valley, key=lambda coord: coord[0])[0] + 1, max(valley, key=lambda coord: coord[1])[1]


def search_goal(valley, blizzards, width, height, start, end, time=0):
    @cache
    def move_blizzards(n):
        blocked = set()
        for (x, y), (dx, dy) in blizzards:
            blocked.add(((x + dx * n) % width, (y + dy * n) % height))
        return blocked

    def get_neighbors(x, y, blocked):
        neighbors = set()
        for neighbor in (x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1), (x, y):
            if neighbor in valley and neighbor not in blocked:
                neighbors.add(neighbor)
        return neighbors

    valley_lcm = lcm(width, height)

    def bfs(start, end, start_time):
        visited = set()
        frontier = deque([(start_time, start)])
        while frontier:
            current_time, current_position = frontier.popleft()
            current_time += 1
            for neighbor in get_neighbors(*current_position, move_blizzards(current_time % valley_lcm)):
                if (current_time, neighbor) not in visited:
                    if neighbor == end:
                        return current_time
                    frontier.append((current_time, neighbor))
                    visited.add((current_time, neighbor))

    return bfs(start, end, time)


def part1(data):
    _, _, width, height = data
    return search_goal(*data, (0, -1), (width - 1, height))


def part2(data):
    _, _, width, height = data
    start, end = (0, -1), (width - 1, height)
    return search_goal(*data, start, end, time=search_goal(*data, end, start, time=part1(data)))


if __name__ == '__main__':
    print(f"Part 1: {part1(parse_input('day24.txt'))}")
    print(f"Part 2: {part2(parse_input('day24.txt'))}")
