#!/usr/bin/env python3
from re import search


def parse_input():
    grammar = {}
    messages = []
    with open('input') as file:
        while (line := file.readline().strip()) != '':
            _id, rule = line.split(':')
            if '"' in rule:
                grammar[int(_id)] = rule[2]
            else:
                grammar[int(_id)] = [[int(nr) for nr in sub_rule.split()] for sub_rule in rule.split('|')]

        while line := file.readline():
            messages.append(line.strip())
    return grammar, messages


def get_regex(grammar, nr):
    if nr == 'a' or nr == 'b':
        return nr
    rules = grammar[nr]
    regex = ''
    for rule in rules:
        for rule_nr in rule:
            regex += get_regex(grammar, rule_nr)
        regex += '|'
    regex = f"({regex[:-1]})"
    while match := search(r'\([^()]\)', regex):
        regex = regex.replace(match.group(0), match.group(0)[1:-1])
    return regex


def part1(grammar, messages):
    pattern = f"^{get_regex(grammar, 0)}$"
    return sum(1 if search(pattern, message) else 0 for message in messages)


def get_loop_regex(grammar, nr, loops=0, max_loops=10):
    if nr == 'a' or nr == 'b':
        return nr

    if nr == 8:
        regex = f"{get_loop_regex(grammar, 42, loops)}+"
    elif nr == 11 and loops < max_loops:
        regex = f"{get_loop_regex(grammar, 42, loops)}{get_loop_regex(grammar, 11, loops + 1)}?{get_loop_regex(grammar, 31, loops)}"
    elif nr == 11:
        regex = f"{get_loop_regex(grammar, 42, loops)}{get_loop_regex(grammar, 31, loops)}"
    else:
        rules = grammar[nr]
        regex = ''
        for rule in rules:
            for rule_nr in rule:
                regex += get_loop_regex(grammar, rule_nr, loops)
            regex += '|'
        regex = regex[:-1]
    regex = f"({regex})"
    while match := search(r'\([^()]\)', regex):
        regex = regex.replace(match.group(0), match.group(0)[1:-1])
    return regex


def part2(grammar, messages):
    pattern = f"^{get_loop_regex(grammar, 0)}$"
    return sum(1 if search(pattern, message) else 0 for message in messages)


def main():
    grammar, messages = parse_input()
    print("Part 1:", part1(grammar, messages))
    print("Part 2:", part2(grammar, messages))


if __name__ == '__main__':
    main()
