#!/usr/bin/env python3

def parse_input(filename):
    with open(filename) as file:
        return [(direction, int(amount)) for line in file for direction, amount in [line.strip().split()]]


def update_tail(head_x, head_y, tail_x, tail_y):
    x_delta = head_x - tail_x
    y_delta = head_y - tail_y

    if abs(x_delta) == 2:
        tail_x += x_delta // 2
        if abs(y_delta) == 1:
            tail_y += y_delta

    if abs(y_delta) == 2:
        tail_y += y_delta // 2
        if abs(x_delta) == 1:
            tail_x += x_delta

    return [tail_x, tail_y]


def count_tail_visits(data, num_nodes):
    assert num_nodes > 1

    nodes = [[0, 0] for _ in range(num_nodes)]
    head = nodes[0]

    visited_by_tail = set()

    for direction, amount in data:
        for _ in range(amount):
            match direction:
                case 'U':
                    head[1] += 1
                case 'D':
                    head[1] -= 1
                case 'R':
                    head[0] += 1
                case 'L':
                    head[0] -= 1

            for i in range(num_nodes - 1):
                nodes[i + 1] = update_tail(*nodes[i], *nodes[i + 1])
            visited_by_tail.add(tuple(nodes[-1]))

    return len(visited_by_tail)


def part1(data):
    return count_tail_visits(data, 2)


def part2(data):
    return count_tail_visits(data, 10)


if __name__ == '__main__':
    print(f"Part 1: {part1(parse_input('day09.txt'))}")
    print(f"Part 2: {part2(parse_input('day09.txt'))}")
