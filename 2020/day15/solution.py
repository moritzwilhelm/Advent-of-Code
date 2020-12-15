#!/usr/bin/env python3


def get_numbers():
    with open('input') as file:
        return [int(number) for number in file.read().split(',')]


def simulate_game(numbers, rounds):
    last_occurrence = {numbers[i]: i + 1 for i in range(len(numbers) - 1)}
    last = numbers[-1]

    for round in range(len(numbers) + 1, rounds + 1):
        if last not in last_occurrence:
            current = 0
        else:
            current = round - 1 - last_occurrence[last]

        last_occurrence[last] = round - 1
        last = current

    return last


def part1(numbers):
    return simulate_game(numbers, 2020)


def part2(numbers):
    return simulate_game(numbers, 30000000)


def main():
    numbers = get_numbers()
    print("Part 1:", part1(numbers))
    print("Part 2:", part2(numbers))


if __name__ == '__main__':
    main()
