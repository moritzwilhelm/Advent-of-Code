#!/usr/bin/env python3


def parse_notes():
    with open('input') as file:
        timestamp = int(file.readline())
        busses = {}
        for index, bus_id in enumerate(file.readline().split(',')):
            if bus_id != 'x':
                busses[index] = int(bus_id)
    return timestamp, busses


def part1(timestamp, busses):
    departures = list(map(lambda index: (busses[index], busses[index] - (timestamp % busses[index])), busses))
    best_bus, waiting_time = min(departures, key=lambda departure: departure[1])
    return best_bus * waiting_time


def chinese_remainder_theorem(busses, modulo):
    res = 0
    for index in busses:
        m_i = modulo // busses[index]
        res += -index * (pow(m_i, -1, busses[index]) * m_i)
        res %= modulo
    return res


def part2(busses):
    # x = -index mod busses[index] for index in busses
    modulo = 1
    for index in busses:
        modulo *= busses[index]
    return chinese_remainder_theorem(busses, modulo)


def main():
    timestamp, busses = parse_notes()
    print("Part 1:", part1(timestamp, busses))
    print("Part 2:", part2(busses))


if __name__ == '__main__':
    main()
