#!/usr/bin/env python3

def get_groups():
    groups = []
    with open('input') as file:
        group = []
        for line in file:
            if line == '\n':
                groups.append(group)
                group = []
            else:
                group.append(set(line.strip()))

    # no empty line at end of file
    groups.append(group)

    return groups


def part1(groups):
    return sum([len(group[0].union(*group)) for group in groups])


def part2(groups):
    return sum([len(group[0].intersection(*group)) for group in groups])


def main():
    groups = get_groups()
    print("Part 1:", part1(groups))
    print("Part 2:", part2(groups))


if __name__ == '__main__':
    main()
