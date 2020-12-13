#!/usr/bin/env python3


def parse_notes():
    with open('input') as file:
        timestamp = int(file.readline())
        bus_ids = []
        for bus_id in file.readline().split(','):
            bus_ids.append(int(bus_id) if bus_id != 'x' else bus_id)
    return timestamp, bus_ids


def part1(timestamp, bus_ids):
    relevant_ids = [bus_id for bus_id in bus_ids if bus_id != 'x']
    departure_times = list(map(lambda _id: _id - (timestamp % _id), relevant_ids))
    waiting_time = min(departure_times)
    departure_id = relevant_ids[departure_times.index(waiting_time)]
    return departure_id * waiting_time


def chinese_remainder_theorem(bus_ids, modulo):
    res = 0
    for i in range(len(bus_ids)):
        if bus_ids[i] != 'x':
            m_i = modulo // bus_ids[i]
            res += -i * (pow(m_i, -1, bus_ids[i]) * m_i)
            res %= modulo
    return res


def part2(bus_ids):
    # x = -index mod value for index, value in enumerate(bus_ids)
    modulo = 1
    for _id in bus_ids:
        if _id != 'x':
            modulo *= _id
    return chinese_remainder_theorem(bus_ids, modulo)


def main():
    timestamp, bus_ids = parse_notes()
    print("Part 1:", part1(timestamp, bus_ids))
    print("Part 2:", part2(bus_ids))


if __name__ == '__main__':
    main()
