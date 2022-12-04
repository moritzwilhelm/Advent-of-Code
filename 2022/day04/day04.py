#!/usr/bin/env python3

def parse_input(filename):
    with open(filename) as file:
        return [(tuple(map(int, item.split('-'))) for item in line.strip().split(',')) for line in file]


def part1(data):
    return sum((x[0] <= y[0] and x[1] >= y[1]) or (y[0] <= x[0] and y[1] >= x[1]) for x, y in data)


def part2(data):
    return sum(max(x[0], y[0]) <= min(x[1], y[1]) for x, y in data)


if __name__ == '__main__':
    print(f"Part 1: {part1(parse_input('day04.txt'))}")
    print(f"Part 2: {part2(parse_input('day04.txt'))}")
