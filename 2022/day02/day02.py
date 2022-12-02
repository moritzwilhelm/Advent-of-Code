#!/usr/bin/env python3

def parse_input(filename):
    with open(filename) as file:
        return [line.strip().split() for line in file]


def part1(data):
    game = {
        ('A', 'X'): 1 + 3,
        ('A', 'Y'): 2 + 6,
        ('A', 'Z'): 3 + 0,
        ('B', 'X'): 1 + 0,
        ('B', 'Y'): 2 + 3,
        ('B', 'Z'): 3 + 6,
        ('C', 'X'): 1 + 6,
        ('C', 'Y'): 2 + 0,
        ('C', 'Z'): 3 + 3,
    }
    return sum(game[player1, player2] for player1, player2 in data)


def part2(data):
    game = {
        ('A', 'X'): 3 + 0,
        ('A', 'Y'): 1 + 3,
        ('A', 'Z'): 2 + 6,
        ('B', 'X'): 1 + 0,
        ('B', 'Y'): 2 + 3,
        ('B', 'Z'): 3 + 6,
        ('C', 'X'): 2 + 0,
        ('C', 'Y'): 3 + 3,
        ('C', 'Z'): 1 + 6,
    }
    return sum(game[player, outcome] for player, outcome in data)


if __name__ == '__main__':
    print(f"Part 1: {part1(parse_input('day02.txt'))}")
    print(f"Part 2: {part2(parse_input('day02.txt'))}")
