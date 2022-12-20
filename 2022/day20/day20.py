#!/usr/bin/env python3
from collections import deque


def parse_input(filename):
    with open(filename) as file:
        return [(int(line), idx) for idx, line in enumerate(file)]


def mix(data, n=1):
    res = deque(data)

    for _ in range(n):
        for item in data:
            value, _ = item
            res.rotate(-res.index(item))
            assert item == res[0]
            res.popleft()
            res.rotate(-value)
            res.appendleft(item)

    return [value for value, _ in res]


def part1(data):
    res = mix(data)
    zero_index = res.index(0)
    return sum(res[(zero_index + i) % len(res)] for i in (1000, 2000, 3000))


def part2(data):
    res = mix([(i * 811589153, j) for i, j in data], 10)
    zero_index = res.index(0)
    return sum(res[(zero_index + i) % len(res)] for i in (1000, 2000, 3000))


if __name__ == "__main__":
    print(f"Part 1: {part1(parse_input('day20.txt'))}")
    print(f"Part 2: {part2(parse_input('day20.txt'))}")
