#!/usr/bin/env python3
from functools import cmp_to_key
from itertools import chain


def parse_input(filename):
    with open(filename) as file:
        return [tuple(map(eval, lines.splitlines())) for lines in file.read().split('\n\n')]


def list_cmp(left, right):
    for i in range(max(len(left), len(right))):
        if i >= len(left):
            return -1
        if i >= len(right):
            return 1

        l, r = left[i], right[i]
        if isinstance(l, int) and isinstance(r, int):
            if l > r:
                return 1
            elif r > l:
                return -1
            else:
                continue
        elif isinstance(l, int) and isinstance(r, list):
            result = list_cmp([l], r)
            if result != 0:
                return result
        elif isinstance(l, list) and isinstance(r, int):
            result = list_cmp(l, [r])
            if result != 0:
                return result
        else:
            result = list_cmp(l, r)
            if result != 0:
                return result

    return 0


def part1(data):
    pair_sum = 0
    for idx, pair in enumerate(data, start=1):
        left, right = pair

        if list_cmp(left, right) == -1:
            pair_sum += idx
    return pair_sum


def part2(data):
    data = list(chain.from_iterable(data))
    data += [[[2]], [[6]]]

    data.sort(key=cmp_to_key(list_cmp))
    return (data.index([[2]]) + 1) * (data.index([[6]]) + 1)


if __name__ == '__main__':
    print(f"Part 1: {part1(parse_input('day13.txt'))}")
    print(f"Part 2: {part2(parse_input('day13.txt'))}")
