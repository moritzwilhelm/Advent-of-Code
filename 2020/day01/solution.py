#!/usr/bin/env python3

def read_inputs():
    with open('input') as file:
        return [int(line.strip()) for line in file]


def part1(values):
    seen = set()
    for i in values:
        if (j := 2020 - i) in seen:
            return i * j
        seen.add(i)


def part2(values):
    seen = set()
    for i in range(len(values)):
        for j in range(i, len(values)):
            if (k := 2020 - values[i] - values[j]) in seen:
                return values[i] * values[j] * k
            seen.add(values[j])
        seen = set()


def main():
    inputs = read_inputs()
    print("Part 1:", part1(inputs))
    print("Part 2:", part2(inputs))


if __name__ == '__main__':
    main()
