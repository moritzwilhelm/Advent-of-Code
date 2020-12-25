#!/usr/bin/env python3


def parse_input():
    with open('input') as file:
        return int(file.readline()), int(file.readline())


def part1(pk1, pk2):
    sk1 = 1
    enc = 1
    while True:
        enc = enc * 7 % 20201227
        if enc == pk1:
            return pk2 ** sk1 % 20201227
        elif enc == pk2:
            return pk1 ** sk1 % 20201227
        sk1 += 1


def part2(pk1, pk2):
    return


def main():
    pk1, pk2 = parse_input()
    print("Part 1:", part1(pk1, pk2))
    print("Part 2:", part2(pk1, pk2))


if __name__ == '__main__':
    main()
