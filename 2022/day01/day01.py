#!/usr/bin/env python3
import heapq


def parse_input(filename):
    with open(filename) as file:
        return [(int(calorie) for calorie in elf.splitlines()) for elf in file.read().split('\n\n')]


def part1(data):
    return max(sum(calories) for calories in data)


def part2(data):
    return sum(heapq.nlargest(3, (sum(calories) for calories in data)))


if __name__ == '__main__':
    print(f"Part 1: {part1(parse_input('day01.txt'))}")
    print(f"Part 2: {part2(parse_input('day01.txt'))}")
