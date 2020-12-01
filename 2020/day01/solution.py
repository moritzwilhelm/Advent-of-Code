#!/usr/bin/env python3

def read_inputs():
    with open('input') as file:
        return [int(line.strip()) for line in file]


def part1(values):
    others = set(values)  # set() works here because there are no duplicates
    for i in values:
        others.remove(i)
        if (j := 2020 - i) in others:
            # print(f"{i} * {j} = {i * j}")
            return i * j


def part2(values):
    others = set(values)
    for i in values:
        others.remove(i)
        for j in others:
            others.remove(j)
            if (k := 2020 - i - j) in others:
                # print(f"{i} * {j} * {k} = {i * j * k}")
                return i * j * k
            others.add(j)


def main():
    inputs = read_inputs()
    print("Part 1:", part1(inputs))
    print("Part 2:", part2(inputs))


if __name__ == '__main__':
    main()
