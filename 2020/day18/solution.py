#!/usr/bin/env python3
from re import search


def parse_input():
    with open('input') as file:
        return [line.strip() for line in file]


def evaluate(line):
    while match := search(r'\d+ [+*] \d+', line):
        line = line.replace(match.group(0), str(eval(match.group(0))), 1)
        while match := search(r'\(\d+\)', line):
            line = line.replace(match.group(0), match.group(0)[1:-1])
    return int(line)


def part1(homework):
    return sum(evaluate(line) for line in homework)


def add_sum_parentheses(line):
    tokens = line.split()
    for i in range(len(tokens)):
        if tokens[i] == '+':
            parentheses_count = 0
            for j in range(i + 1, len(tokens)):
                parentheses_count += tokens[j].count('(') - tokens[j].count(')')
                if parentheses_count <= 0:
                    tokens[j] += ')'
                    break
            parentheses_count = 0
            for j in range(i - 1, -1, -1):
                parentheses_count += tokens[j].count(')') - tokens[j].count('(')
                if parentheses_count <= 0:
                    tokens[j] = '(' + tokens[j]
                    break
    return ' '.join(tokens)


def part2(homework):
    return sum(evaluate(add_sum_parentheses(line)) for line in homework)


def main():
    homework = parse_input()
    print("Part 1:", part1(homework))
    print("Part 2:", part2(homework))


if __name__ == '__main__':
    main()
