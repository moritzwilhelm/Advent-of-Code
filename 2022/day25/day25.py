#!/usr/bin/env python3

def parse_input(filename):
    with open(filename) as file:
        return [line.strip() for line in file]


def to_decimal(number):
    res = 0
    for c in number:
        res *= 5
        res += '=-012'.index(c) - 2
    return res


def to_snafu(number):
    res = []
    while number:
        number, remainder = divmod(number + 2, 5)
        res.append('=-012'[remainder])
    return ''.join(reversed(res))


def part1(data):
    return to_snafu(sum(to_decimal(number) for number in data))


def part2(data):
    return 'https://adventofcode.com/2022/day/25/answer'


if __name__ == '__main__':
    print(f"Part 1: {part1(parse_input('day25.txt'))}")
    print(f"Part 2: {part2(parse_input('day25.txt'))}")
