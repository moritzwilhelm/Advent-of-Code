#!/usr/bin/env python3
import itertools
import re
from collections import defaultdict
from functools import cache
from math import inf

VALVE_PATTERN = re.compile(
    r"Valve ([A-Z][A-Z]) has flow rate=(\d+); tunnels? leads? to valves? (.*)")


def parse_input(filename):
    valves = set()
    flow_rates = {}
    distances = defaultdict(lambda: inf)
    with open(filename) as file:
        for valve, flow_rate, neighbors in VALVE_PATTERN.findall(file.read()):
            valves.add(valve)
            if flow_rate != '0':
                flow_rates[valve] = int(flow_rate)
            for neighbor in neighbors.split(', '):
                distances[valve, neighbor] = 1

    # floyd-warshall
    for k, i, j in itertools.product(valves, valves, valves):
        distances[i, j] = min(distances[i, j], distances[i, k] + distances[k, j])

    return flow_rates, distances


def compute_max_pressure(flow_rates, distances, time, with_elefant=False):
    @cache
    def _compute_max_pressure(time_left, start='AA', open_valves=frozenset(flow_rates), elefant=False):
        candidates = []
        for valve in open_valves:
            distance = distances[start, valve]
            if distance < time_left:
                pressure = flow_rates[valve] * (time_left - distance - 1)
                candidates.append(
                    pressure + _compute_max_pressure(time_left - distance - 1, valve, open_valves - {valve}, elefant))

        if elefant:
            candidates.append(_compute_max_pressure(26, 'AA', open_valves, elefant=False))
        return max(candidates) if candidates else 0

    return _compute_max_pressure(time, elefant=with_elefant)


def part1(data):
    return compute_max_pressure(*data, 30)


def part2(data):
    return compute_max_pressure(*data, 26, with_elefant=True)


if __name__ == '__main__':
    print(f"Part 1: {part1(parse_input('day16.txt'))}")
    print(f"Part 2: {part2(parse_input('day16.txt'))}")
