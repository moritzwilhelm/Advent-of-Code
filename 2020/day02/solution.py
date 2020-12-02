#!/usr/bin/env python3

def parse_inputs():
    inputs = []
    with open('input') as file:
        for line in file:
            policy, password = line.split(':')
            policy_range, policy_char = policy.split()
            policy_min, policy_max = policy_range.split('-')
            inputs.append(((int(policy_min), int(policy_max), policy_char), password.strip()))
    return inputs


def part1(database_entries):
    count = 0
    for policy, password in database_entries:
        min, max, char = policy
        if min <= password.count(char) <= max:
            count += 1
    return count


def part2(database_entries):
    count = 0
    for policy, password in database_entries:
        min, max, char = policy
        if (password[min - 1] == char) ^ (password[max - 1] == char):
            count += 1
    return count


def main():
    inputs = parse_inputs()
    print("Part 1:", part1(inputs))
    print("Part 2:", part2(inputs))


if __name__ == '__main__':
    main()
