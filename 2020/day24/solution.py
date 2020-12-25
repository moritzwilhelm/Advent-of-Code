#!/usr/bin/env python3
from collections import defaultdict


def parse_input():
    black_tiles = set()
    with open('input') as file:
        for line in file:
            current = line.strip()
            tile = [0, 0]
            while current:
                if current.startswith('e'):
                    tile[0] += 1
                    current = current[1:]
                elif current.startswith('w'):
                    tile[0] -= 1
                    current = current[1:]
                elif current.startswith('se'):
                    tile[1] += 1
                    current = current[2:]
                elif current.startswith('nw'):
                    tile[1] -= 1
                    current = current[2:]
                elif current.startswith('sw'):
                    tile[0] -= 1
                    tile[1] += 1
                    current = current[2:]
                elif current.startswith('ne'):
                    tile[0] += 1
                    tile[1] -= 1
                    current = current[2:]
                else:
                    exit(f"Bad input '{line.strip()}'")
            tile = tuple(tile)
            if tile in black_tiles:
                black_tiles.remove(tile)
            else:
                black_tiles.add(tile)
    return black_tiles


def part1(black_tiles):
    return len(black_tiles)


def simulate_flipping(tiles, rounds=100):
    for _ in range(rounds):
        neighbor_count = defaultdict(int)
        for tile in tiles:
            neighbor_count[tuple([tile[0] - 1, tile[1]])] += 1
            neighbor_count[tuple([tile[0] + 1, tile[1]])] += 1
            neighbor_count[tuple([tile[0], tile[1] - 1])] += 1
            neighbor_count[tuple([tile[0], tile[1] + 1])] += 1
            neighbor_count[tuple([tile[0] - 1, tile[1] + 1])] += 1
            neighbor_count[tuple([tile[0] + 1, tile[1] - 1])] += 1
        new_tiles = set()
        for tile in neighbor_count:
            if tile in tiles and 1 <= neighbor_count[tile] <= 2:
                new_tiles.add(tile)
            elif tile not in tiles and neighbor_count[tile] == 2:
                new_tiles.add(tile)
        tiles = new_tiles
    return tiles


def part2(black_tiles):
    return len(simulate_flipping(black_tiles))


def main():
    black_tiles = parse_input()
    print("Part 1:", part1(black_tiles))
    print("Part 2:", part2(black_tiles))


if __name__ == '__main__':
    main()
