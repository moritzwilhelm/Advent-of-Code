#!/usr/bin/env python3


def get_instructions():
    instructions = []
    with open('input') as file:
        for line in file:
            action = line[0]
            value = int(line[1:].strip())
            instructions.append((action, value))
    return instructions


def perform_action(instruction, north, east, direction):
    action, value = instruction
    if action == 'N':
        north += value
        return north, east, direction
    if action == 'S':
        north -= value
        return north, east, direction
    if action == 'E':
        east += value
        return north, east, direction
    if action == 'W':
        east -= value
        return north, east, direction
    if action == 'F':
        return perform_action((['N', 'E', 'S', 'W'][direction], value), north, east, direction)
    if action == 'R':
        return north, east, (direction + (value // 90)) % 4
    if action == 'L':
        return north, east, (direction - (value // 90)) % 4


def part1(instructions):
    north = 0
    east = 0
    direction = 1
    for instruction in instructions:
        north, east, direction = perform_action(instruction, north, east, direction)
    return abs(north) + abs(east)


def perform_action_waypoint(instruction, north, east, waypoint):
    action, value = instruction
    if action == 'N':
        waypoint[0] += value
    elif action == 'S':
        waypoint[2] += value
    elif action == 'E':
        waypoint[1] += value
    elif action == 'W':
        waypoint[3] += value
    elif action == 'F':
        north += value * (waypoint[0] - waypoint[2])
        east += value * (waypoint[1] - waypoint[3])
    elif action == 'R':
        for i in range((value // 90) % 4):
            waypoint = [waypoint[3], waypoint[0], waypoint[1], waypoint[2]]
    elif action == 'L':
        for i in range((value // 90) % 4):
            waypoint = [waypoint[1], waypoint[2], waypoint[3], waypoint[0]]
    return north, east, waypoint


def part2(instructions):
    north = 0
    east = 0
    waypoint = [1, 10, 0, 0]
    for instruction in instructions:
        north, east, waypoint = perform_action_waypoint(instruction, north, east, waypoint)
    return abs(north) + abs(east)


def main():
    instructions = get_instructions()
    print("Part 1:", part1(instructions))
    print("Part 2:", part2(instructions))


if __name__ == '__main__':
    main()
