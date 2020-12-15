#!/usr/bin/env python3


def get_numbers():
    with open('input') as file:
        return [int(number) for number in file.read().split(',')]


def simulate_game(numbers, rounds):
    number = numbers[-1]
    occurrences = {numbers[i]: (i + 1, 0) for i in range(len(numbers))}

    for i in range(len(numbers) + 1, rounds + 1):
        # compute ith number spoken
        if occurrences[number][1] == 0:
            number = 0
        else:
            number = occurrences[number][0] - occurrences[number][1]

        # update age of number
        if number in occurrences:
            occurrences[number] = (i, occurrences[number][0])
        else:
            occurrences[number] = (i, 0)

    return number


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
