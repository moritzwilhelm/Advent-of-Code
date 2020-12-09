#!/usr/bin/env python3

def parse_program():
    program = []
    with open('input') as file:
        for line in file:
            line = line.strip()
            operation, argument = line.split()
            program.append((operation, int(argument)))

    return program


def execute_program(program):
    accumulator = 0
    instruction = 0
    visited = set()
    while instruction < len(program):
        operation, argument = program[instruction]
        if instruction in visited:
            return False, accumulator

        visited.add(instruction)

        if operation == 'jmp':
            instruction += argument
            continue

        if operation == 'acc':
            accumulator += argument

        instruction += 1

    return True, accumulator


def part1(program):
    return execute_program(program)[1]


def part2(program):
    for i in range(len(program)):
        operation, argument = program[i]
        if operation == 'acc':
            continue
        if operation == 'nop':
            before, after = 'nop', 'jmp'
        else:
            before, after = 'jmp', 'nop'
        program[i] = (after, argument)
        terminated, accumulator = execute_program(program)
        if terminated:
            return accumulator
        program[i] = (before, argument)


def main():
    program = parse_program()
    print("Part 1:", part1(program))
    print("Part 2:", part2(program))


if __name__ == '__main__':
    main()
