#!/usr/bin/env python3
from collections import defaultdict


def get_adapters():
    with open('input') as file:
        adapters = sorted(int(line.strip()) for line in file)
    return [0] + adapters + [adapters[-1] + 3]


def part1(adapters):
    differences = defaultdict(int)
    for i in range(1, len(adapters)):
        differences[adapters[i] - adapters[i - 1]] += 1
    return differences[1] * differences[3]


def part2(adapters):
    arrangement_count = [1] + adapters[-1] * [0]
    for i in adapters[1:]:
        start = i - 3 if i >= 3 else 0
        arrangement_count[i] = sum(arrangement_count[start:i])
    return arrangement_count[-1]


def main():
    adapters = get_adapters()
    print("Part 1:", part1(adapters))
    print("Part 2:", part2(adapters))


if __name__ == '__main__':
    main()
