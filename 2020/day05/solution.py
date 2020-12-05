#!/usr/bin/env python3

def parse_passes():
    pass_ids = []
    with open('input') as file:
        for line in file:
            line = line.strip()
            row = int(line[:7].replace('B', '1').replace('F', '0'), 2)
            column = int(line[7:].replace('R', '1').replace('L', '0'), 2)
            pass_ids.append(row * 8 + column)
    return pass_ids


def part1(pass_ids):
    return max(pass_ids)


def part2(pass_ids):
    ids = sorted(pass_ids)
    for i in range(len(ids) - 1):
        if ids[i + 1] - ids[i] == 2:
            return ids[i + 1] - 1


def main():
    pass_ids = parse_passes()
    print("Part 1:", part1(pass_ids))
    print("Part 2:", part2(pass_ids))


if __name__ == '__main__':
    main()
