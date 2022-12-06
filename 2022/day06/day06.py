#!/usr/bin/env python3
from collections import deque


def parse_input(filename):
    with open(filename) as file:
        return file.readline().strip()


def find_marker(datastream, length):
    window = deque(datastream[:length])
    for idx, c in enumerate(datastream[length:], start=length):
        if len(set(window)) == length:
            return idx
        else:
            window.popleft()
            window.append(c)


def part1(data):
    return find_marker(data, 4)


def part2(data):
    return find_marker(data, 14)


if __name__ == '__main__':
    print(f"Part 1: {part1(parse_input('day06.txt'))}")
    print(f"Part 2: {part2(parse_input('day06.txt'))}")
