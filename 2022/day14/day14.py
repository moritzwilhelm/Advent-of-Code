#!/usr/bin/env python3

def parse_input(filename):
    rocks = set()
    with open(filename) as file:
        for line in file:
            points = list(map(
                lambda p: (int(p[0]), int(p[1])), [point.strip().split(',') for point in line.strip().split(' -> ')]
            ))
            previous_x, previous_y = points[0]
            rocks.add(points[0])
            for x, y in points[1:]:
                if previous_x > x:
                    for i in range(previous_x - x):
                        rocks.add((x + i, y))
                elif previous_x < x:
                    for i in range(x - previous_x):
                        rocks.add((x - i, y))
                elif previous_y > y:
                    for i in range(previous_y - y):
                        rocks.add((x, y + i))
                elif y > previous_y:
                    for i in range(y - previous_y):
                        rocks.add((x, y - i))

                previous_x, previous_y = x, y

    return rocks


def part1(data):
    sand_x, sand_y = (500, 0)
    sand_count = 0
    void_border = max(data, key=lambda p: p[1])[1]
    while sand_y <= void_border:
        if (sand_x, sand_y + 1) not in data:
            sand_y += 1
        elif (sand_x - 1, sand_y + 1) not in data:
            sand_x -= 1
            sand_y += 1
        elif (sand_x + 1, sand_y + 1) not in data:
            sand_x += 1
            sand_y += 1
        else:
            data.add((sand_x, sand_y))
            sand_count += 1
            sand_x = 500
            sand_y = 0
    return sand_count


def part2(data):
    sand_x, sand_y = (500, 0)
    sand_count = 0
    floor_level = max(data, key=lambda p: p[1])[1] + 2
    while (500, 0) not in data:
        if sand_y + 1 == floor_level:
            data.add((sand_x, sand_y))
            sand_count += 1
            sand_x = 500
            sand_y = 0
        elif (sand_x, sand_y + 1) not in data:
            sand_y += 1
        elif (sand_x - 1, sand_y + 1) not in data:
            sand_x -= 1
            sand_y += 1
        elif (sand_x + 1, sand_y + 1) not in data:
            sand_x += 1
            sand_y += 1
        else:
            data.add((sand_x, sand_y))
            sand_count += 1
            sand_x = 500
            sand_y = 0
    return sand_count


if __name__ == '__main__':
    print(f"Part 1: {part1(parse_input('day14.txt'))}")
    print(f"Part 2: {part2(parse_input('day14.txt'))}")
