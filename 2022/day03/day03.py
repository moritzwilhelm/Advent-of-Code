#!/usr/bin/env python3

def parse_input(filename):
    with open(filename) as file:
        return [line.strip() for line in file]


def char_to_priority(c):
    if 'a' <= c <= 'z':
        return ord(c) - ord('a') + 1
    else:
        return ord(c) - ord('A') + 27


def get_group_priority(*items):
    return char_to_priority(set.intersection(*map(set, items)).pop())


def part1(data):
    return sum(get_group_priority(rucksack[:len(rucksack) // 2], rucksack[len(rucksack) // 2:]) for rucksack in data)


def part2(data):
    return sum(get_group_priority(*data[i:i + 3]) for i in range(0, len(data), 3))


if __name__ == '__main__':
    print(f"Part 1: {part1(parse_input('day03.txt'))}")
    print(f"Part 2: {part2(parse_input('day03.txt'))}")
