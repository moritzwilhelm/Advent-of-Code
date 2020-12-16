#!/usr/bin/env python3
from collections import defaultdict
from functools import reduce
from re import match as regex_match


def parse_input():
    fields = {}
    nearby_tickets = []
    with open('input') as file:
        # parse rules
        while (line := file.readline().strip()) != '':
            match = regex_match('([a-z ]+): ([0-9]+-[0-9]+) or ([0-9]+-[0-9]+)', line)
            start1, end1 = match.group(2).split('-')
            start2, end2 = match.group(3).split('-')
            fields[match.group(1)] = (range(int(start1), int(end1) + 1), range(int(start2), int(end2) + 1))

        # parse own ticket
        file.readline()
        ticket = [int(value) for value in file.readline().strip().split(',')]

        # parse nearby tickets
        file.readline()
        file.readline()
        while (line := file.readline().strip()) != '':
            nearby_tickets.append([int(value) for value in line.split(',')])
    return fields, ticket, nearby_tickets


def part1(fields, nearby_tickets):
    invalid_values = []
    for ticket in nearby_tickets:
        invalid_values += get_invalid_ticket_values(ticket, fields)
    return sum(invalid_values)


def get_invalid_ticket_values(ticket, fields):
    invalid_values = []
    for value in ticket:
        for field in fields:
            if value in fields[field][0] or value in fields[field][1]:
                break
        else:
            invalid_values.append(value)
    return invalid_values


def part2(fields, ticket, nearby_tickets):
    # get all valid tickets
    valid_tickets = []
    for nearby_ticket in nearby_tickets:
        if not get_invalid_ticket_values(nearby_ticket, fields):
            valid_tickets.append(nearby_ticket)

    # get all possible fields per index
    field_at = defaultdict(list)
    for i in range(len(ticket)):
        for field in fields:
            for valid_ticket in valid_tickets:
                if valid_ticket[i] not in fields[field][0] and valid_ticket[i] not in fields[field][1]:
                    break
            else:
                field_at[i].append(field)

    # filter field_at until only one field left per index
    while not all(len(field_at[i]) == 1 for i in field_at):
        for i in field_at:
            if len(field_at[i]) == 1:
                field = field_at[i][0]
                for other in field_at:
                    if other != i and field in field_at[other]:
                        field_at[other].remove(field)

    return reduce(lambda x, y: x * y, (ticket[i] for i in field_at if field_at[i][0].startswith('departure')))


def main():
    fields, ticket, nearby_tickets = parse_input()
    print("Part 1:", part1(fields, nearby_tickets))
    print("Part 2:", part2(fields, ticket, nearby_tickets))


if __name__ == '__main__':
    main()
