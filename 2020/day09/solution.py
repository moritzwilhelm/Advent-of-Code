#!/usr/bin/env python3

def parse_xmas():
    preamble = []
    rest = []
    with open('input') as file:
        for i in range(25):
            line = file.readline().strip()
            preamble.append(int(line))
        while line := file.readline():
            rest.append(int(line.strip()))
    return preamble, rest


def part1(preamble, rest):
    for number in rest:
        for i in preamble:
            if number - i in preamble:
                break
        else:
            return number
        preamble = preamble[1:]
        preamble += [number]

    return None


def part2(preamble, rest):
    values = preamble + rest
    invalid = part1(preamble, rest)
    contiguous_values = []

    while values:
        set_sum = sum(contiguous_values)
        if set_sum > invalid:
            contiguous_values.pop(0)
        elif set_sum < invalid:
            contiguous_values.append(values.pop(0))
        else:
            return min(contiguous_values) + max(contiguous_values)


def main():
    preamble, rest = parse_xmas()
    print("Part 1:", part1(preamble, rest))
    print("Part 2:", part2(preamble, rest))


if __name__ == '__main__':
    main()
