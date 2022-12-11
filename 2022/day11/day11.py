#!/usr/bin/env python3
import heapq
import re
from collections import defaultdict, deque
from math import lcm
from operator import mul

MONKEY_REGEX = re.compile(r"""Monkey (\d+):
  Starting items: (\d+(, \d+)*)
  Operation: new = (.*)
  Test: divisible by (\d+)
    If true: throw to monkey (\d+)
    If false: throw to monkey (\d+)""")


def parse_input(filename):
    items = {}
    monkey_actions = {}
    divisors = set()
    with open(filename) as file:
        for match in MONKEY_REGEX.findall(file.read()):
            monkey_id = int(match[0])
            items[monkey_id] = deque(map(int, match[1].split(', ')))
            operation = eval(f"lambda old: {match[3]}")
            divisor = int(match[4])
            true_monkey = int(match[5])
            false_monkey = int(match[6])
            monkey_actions[monkey_id] = (operation, divisor, true_monkey, false_monkey)
            divisors.add(divisor)

    return items, monkey_actions, lcm(*divisors)


def compute_monkey_business(rounds, data, dividing_worry_level=True):
    items, monkey_actions, divisors_lcm = data
    inspection_count = defaultdict(int)

    for _ in range(rounds):
        for monkey in monkey_actions:
            while items[monkey]:
                inspection_count[monkey] += 1
                operation, divisor, true_monkey, false_monkey = monkey_actions[monkey]
                old = items[monkey].popleft()
                new = operation(old) // 3 if dividing_worry_level else operation(old) % divisors_lcm
                items[true_monkey if new % divisor == 0 else false_monkey].append(new)

    return mul(*heapq.nlargest(2, inspection_count.values()))


def part1(data):
    return compute_monkey_business(20, data)


def part2(data):
    return compute_monkey_business(10000, data, False)


if __name__ == '__main__':
    print(f"Part 1: {part1(parse_input('day11.txt'))}")
    print(f"Part 2: {part2(parse_input('day11.txt'))}")
