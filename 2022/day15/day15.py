#!/usr/bin/env python3
import heapq
import re
from collections import defaultdict

COORDINATE_REGEX = re.compile(r"x=(-?\d+), y=(-?\d+)")


def parse_input(filename):
    blocked_ranges = defaultdict(list)
    sensors_range = {}
    beacons = set()
    with open(filename) as file:
        for line in file:
            match = COORDINATE_REGEX.findall(line)
            sensor_x = int(match[0][0])
            sensor_y = int(match[0][1])
            beacon_x = int(match[1][0])
            beacon_y = int(match[1][1])

            beacons.add((beacon_x, beacon_y))
            distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
            sensors_range[(sensor_x, sensor_y)] = distance

            for dy in range(-distance, distance + 1):
                if sensor_y + dy in range(4000001):
                    heapq.heappush(blocked_ranges[sensor_y + dy],
                                   (sensor_x - (distance - abs(dy)), sensor_x + (distance - abs(dy)) + 1))

    return blocked_ranges, sensors_range, beacons


def part1(data):
    blocked_ranges, sensors_range, beacons = data
    res = 0
    for column in range(min(sensor[0] - distance for sensor, distance in sensors_range.items()),
                        max(sensor[0] + distance for sensor, distance in sensors_range.items())):
        if (column, 2000000) not in beacons:
            for start, end in blocked_ranges[2000000]:
                if start <= column < end:
                    res += 1
                    break
    return res


def part2(data):
    blocked_ranges, _, _ = data
    for row in range(4000001):
        current = 0
        while current < 4000001 and blocked_ranges[row]:
            start, end = heapq.heappop(blocked_ranges[row])
            if start <= current:
                current = max(current, end)
            else:
                return current * 4000000 + row


if __name__ == '__main__':
    print(f"Part 1: {part1(parse_input('day15.txt'))}")
    print(f"Part 2: {part2(parse_input('day15.txt'))}")
