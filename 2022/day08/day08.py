#!/usr/bin/env python3

def parse_input(filename):
    with open(filename) as file:
        return [[int(tree) for tree in line.strip()] for line in file]


def is_visible(data, i, j):
    return (all(data[k][j] < data[i][j] for k in range(i - 1, -1, -1)) or  # north
            all(data[k][j] < data[i][j] for k in range(i + 1, len(data))) or  # south
            all(data[i][k] < data[i][j] for k in range(j + 1, len(data[0]))) or  # east
            all(data[i][k] < data[i][j] for k in range(j - 1, -1, -1)))  # west


def part1(data):
    exterior_trees = (len(data) - 1) * 4 if len(data) > 1 else 1
    interior_trees = sum(is_visible(data, i, j) for i in range(1, len(data) - 1) for j in range(1, len(data) - 1))
    return exterior_trees + interior_trees


def compute_scenic_score(data, i, j):
    north_score = 0
    for k in range(i - 1, -1, -1):
        north_score += 1
        if data[k][j] >= data[i][j]:
            break

    south_score = 0
    for k in range(i + 1, len(data)):
        south_score += 1
        if data[k][j] >= data[i][j]:
            break

    east_score = 0
    for k in range(j + 1, len(data[0])):
        east_score += 1
        if data[i][k] >= data[i][j]:
            break

    west_score = 0
    for k in range(j - 1, -1, -1):
        west_score += 1
        if data[i][k] >= data[i][j]:
            break

    return north_score * south_score * east_score * west_score


def part2(data):
    return max(compute_scenic_score(data, i, j) for i in range(1, len(data) - 1) for j in range(1, len(data) - 1))


if __name__ == '__main__':
    print(f"Part 1: {part1(parse_input('day08.txt'))}")
    print(f"Part 2: {part2(parse_input('day08.txt'))}")
