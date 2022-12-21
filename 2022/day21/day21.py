#!/usr/bin/env python3
"""
This solution makes use of the sympy package to solve an equation to find a solution for part 2.
It solves the equation (left - right = 0) with "left" and "right" being defined by the monkey called "root".
monkey[root] := left == right <=> left - right == 0
"""
from sympy import solve, parse_expr


def parse_input(filename):
    jobs = {}
    with open(filename) as file:
        for line in file:
            monkey, job = line.strip().split(':')
            jobs[monkey] = job.strip()

    return jobs


def resolve(data, job):
    if job.isdigit() or job == 'x':
        return job
    elif job in data:
        return resolve(data, data[job])
    else:
        left, operand, right = job.split()
        return f"({resolve(data, left)}{operand}{resolve(data, right)})"


def part1(data):
    return eval(resolve(data, data['root']))


def part2(data):
    data['humn'] = 'x'
    left, _, right = data['root'].split()
    return solve(parse_expr(resolve(data, left)) - parse_expr(resolve(data, right)))


if __name__ == '__main__':
    print(f"Part 1: {part1(parse_input('day21.txt'))}")
    print(f"Part 2: {part2(parse_input('day21.txt'))}")
