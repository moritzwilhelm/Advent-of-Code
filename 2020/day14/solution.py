#!/usr/bin/env python3
from re import match as regex_match


def parse_program():
    program = []
    with open('input') as file:
        for line in file:
            if line.startswith('mask'):
                program.append(('mask', line.split('=')[1].strip()))
            else:
                match = regex_match('mem\\[([0-9]+)] = ([0-9]+)', line)
                program.append((int(match.group(1)), int(match.group(2))))
    return program


def apply_mask_on_value(mask, value):
    value = format(value, '036b')
    res = ''
    for index in range(len(mask)):
        if mask[index] == 'X':
            res += value[index]
        else:
            res += mask[index]
    return int(res, 2)


def part1(program):
    mem = {}
    for instruction in program:
        if instruction[0] == 'mask':
            mask = instruction[1]
        else:
            address, value = instruction
            mem[address] = apply_mask_on_value(mask, value)
    return sum(mem.values())


def mask_recursion(mask, address, index, res):
    if index == len(mask):
        return [res]
    elif mask[index] == '0':
        return mask_recursion(mask, address, index + 1, res + address[index])
    elif mask[index] == '1':
        return mask_recursion(mask, address, index + 1, res + '1')
    else:
        return mask_recursion(mask, address, index + 1, res + '0') + mask_recursion(mask, address, index + 1, res + '1')


def apply_mask_on_address(mask, address):
    return mask_recursion(mask, format(address, '036b'), 0, '')


def part2(program):
    mem = {}
    for instruction in program:
        if instruction[0] == 'mask':
            mask = instruction[1]
        else:
            for address in apply_mask_on_address(mask, instruction[0]):
                mem[address] = instruction[1]
    return sum(mem.values())


def main():
    program = parse_program()
    print("Part 1:", part1(program))
    print("Part 2:", part2(program))


if __name__ == '__main__':
    main()
