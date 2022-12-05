#!/usr/bin/env python3

def parse_input(filename):
    with open(filename) as file:
        serialized_stack, serialized_operations = file.read().split('\n\n')

    # parse stacks
    serialized_stack_lines = serialized_stack.splitlines()
    stacks = [[] for _ in range(len(serialized_stack_lines[-1].split()))]
    for line in reversed(serialized_stack_lines[:-1]):
        for i in range(1, len(line), 4):
            if line[i].isalpha():
                stacks[i // 4].append(line[i])

    # parse operations
    operations = []
    for line in serialized_operations.splitlines():
        _, number, _, from_stack, _, to_stack = line.strip().split()
        operations.append((int(number), int(from_stack) - 1, int(to_stack) - 1))

    return stacks, operations


def part1(data):
    stacks, operations = data
    for number, from_stack, to_stack in operations:
        for _ in range(number):
            stacks[to_stack].append(stacks[from_stack].pop())
    return ''.join(stack.pop() for stack in stacks)


def part2(data):
    stacks, operations = data
    temp = []
    for number, from_stack, to_stack in operations:
        for _ in range(number):
            temp.append(stacks[from_stack].pop())
        for _ in range(number):
            stacks[to_stack].append(temp.pop())
    return ''.join(stack.pop() for stack in stacks)


if __name__ == '__main__':
    print(f"Part 1: {part1(parse_input('day05.txt'))}")
    print(f"Part 2: {part2(parse_input('day05.txt'))}")
