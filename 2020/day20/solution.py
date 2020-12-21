#!/usr/bin/env python3
from functools import reduce
from operator import mul


def parse_input():
    tiles = {}
    with open('input') as file:
        tiles_str = file.read().split('\n\n')
        for tile_str in tiles_str:
            tile = tile_str.split('\n')
            _id = tile[0][5:-1]
            tile = tile[1:]
            tiles[_id] = tile
    return tiles


def get_adjacent_tile_count(tiles, tile):
    borders = [
        tiles[tile][0],  # top
        ''.join([line[-1] for line in tiles[tile]]),  # right
        tiles[tile][-1][::-1],  # bottom
        ''.join([line[0] for line in tiles[tile]])[::-1]  # left
    ]
    border_match_count = 0

    for other in tiles:
        if other != tile:
            other_borders = [
                tiles[other][0],  # top
                ''.join([line[-1] for line in tiles[other]]),  # right
                tiles[other][-1][::-1],  # bottom
                ''.join([line[0] for line in tiles[other]])[::-1]  # left
            ]
            for border in borders:
                for other_border in other_borders:
                    if border == other_border or border == other_border[::-1]:
                        border_match_count += 1
                        break
                else:
                    continue
                break
    return border_match_count


def part1(tiles):
    same_edges_count = {}
    for tile in tiles:
        same_edges_count[tile] = get_adjacent_tile_count(tiles, tile)

    return reduce(mul, (int(count) for count in same_edges_count if same_edges_count[count] == 2))


def part2(tiles):
    pass


def main():
    tiles = parse_input()
    print("Part 1:", part1(tiles))
    print("Part 2:", part2(tiles))


if __name__ == '__main__':
    main()
