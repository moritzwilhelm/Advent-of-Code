#!/usr/bin/env python3

def parse_input(filename):
    operations = []
    with open(filename) as file:
        for line in file:
            operation = line.strip().split()
            if len(operation) == 1:
                operations.append(operation[0])
            else:
                operations.append((operation[0], int(operation[1])))
    return operations


def part1(data):
    X = 1
    cycle = 1
    interesting_strengths_sum = 0
    for operation in data:
        if (cycle - 20) % 40 == 0:
            interesting_strengths_sum += cycle * X
        if operation == 'noop':
            cycle += 1
        else:
            _, value = operation
            cycle += 1
            if (cycle - 20) % 40 == 0:
                interesting_strengths_sum += cycle * X
            cycle += 1
            X += value
    return interesting_strengths_sum


def part2(data):
    sprite = 1
    pixel = 0
    crt = []
    for operation in data:
        crt.append('#' if sprite - 1 <= (pixel % 40) <= sprite + 1 else '.')
        if operation == 'noop':
            pixel += 1
        else:
            _, value = operation
            pixel += 1
            crt.append('#' if sprite - 1 <= (pixel % 40) <= sprite + 1 else '.')
            pixel += 1
            sprite += value
    return '\n' + '\n'.join(''.join(crt[i:i + 40]) for i in range(0, len(crt), 40))


if __name__ == '__main__':
    print(f"Part 1: {part1(parse_input('day10.txt'))}")
    print(f"Part 2: {part2(parse_input('day10.txt'))}")
