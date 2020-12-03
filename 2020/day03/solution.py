#!/usr/bin/env python3

def build_map():
    with open('input') as file:
        return [line.strip() for line in file]


def get_treecount_on_slope(map, right, down):
    map_height = len(map)
    map_width = len(map[0])
    number_trees = 0
    for i in range(down, map_height, down):
        if map[i][(right * (i // down)) % map_width] == '#':
            number_trees += 1
    return number_trees


def part1(map):
    return get_treecount_on_slope(map, 3, 1)


def part2(map):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    tree_product = 1
    for right, down in slopes:
        tree_product *= get_treecount_on_slope(map, right, down)
    return tree_product


def main():
    map = build_map()
    print("Part 1:", part1(map))
    print("Part 2:", part2(map))


if __name__ == '__main__':
    main()
