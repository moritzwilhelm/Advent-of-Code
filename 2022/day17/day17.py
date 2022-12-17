#!/usr/bin/env python3
from collections import defaultdict


def parse_input(filename):
    with open(filename) as file:
        return file.readline().strip()


class Simulation:
    def __init__(self, jet_pattern):
        self.jet_index = 0
        self.jet_pattern = [-1 if j == '<' else 1 for j in jet_pattern]
        self.stopped_rocks = {(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0)}
        self.rock_count = 0
        self.current_rock = 0
        self.cache = defaultdict(list)

    def get_tower_size(self):
        return max(self.stopped_rocks, key=lambda x: x[1])[1]

    def _spawn_rock(self):
        self.rock_count += 1
        return 2, self.get_tower_size() + 4

    def _will_collide_with_rocks(self, rocks):
        for rx, ry in rocks:
            if (rx, ry - 1) in self.stopped_rocks:
                return True
        return False

    def _will_collide_with_rocks_or_wall(self, movement, rocks):
        for rx, ry in rocks:
            if (rx + movement, ry) in self.stopped_rocks or (rx + movement) < 0 or (rx + movement) >= 7:
                return True
        return False

    def _get_top_indexes(self):
        res = []
        top = self.get_tower_size()
        for i in range(7):
            res.append(max(y for x, y in self.stopped_rocks if x == i) - top)
        return tuple(res)

    def _simulation_hash(self):
        return self.current_rock, self.jet_index, self._get_top_indexes()

    def simulate_falling_rock(self):
        spawn_x, spawn_y = self._spawn_rock()

        match self.current_rock:
            case 0:
                rocks = {(spawn_x, spawn_y), (spawn_x + 1, spawn_y), (spawn_x + 2, spawn_y), (spawn_x + 3, spawn_y)}
            case 1:
                rocks = {(spawn_x, spawn_y + 1), (spawn_x + 1, spawn_y + 1), (spawn_x + 2, spawn_y + 1),
                         (spawn_x + 1, spawn_y), (spawn_x + 1, spawn_y + 2)}
            case 2:
                rocks = {(spawn_x, spawn_y), (spawn_x + 1, spawn_y), (spawn_x + 2, spawn_y), (spawn_x + 2, spawn_y + 1),
                         (spawn_x + 2, spawn_y + 2)}
            case 3:
                rocks = {(spawn_x, spawn_y), (spawn_x, spawn_y + 1), (spawn_x, spawn_y + 2), (spawn_x, spawn_y + 3)}
            case 4:
                rocks = {(spawn_x, spawn_y), (spawn_x, spawn_y + 1), (spawn_x + 1, spawn_y), (spawn_x + 1, spawn_y + 1)}

        while True:
            if not self._will_collide_with_rocks_or_wall(self.jet_pattern[self.jet_index], rocks):
                rocks = {(r_x + self.jet_pattern[self.jet_index], r_y) for r_x, r_y in rocks}

            self.jet_index += 1
            self.jet_index %= len(self.jet_pattern)

            if not self._will_collide_with_rocks(rocks):
                rocks = {(r_x, r_y - 1) for r_x, r_y in rocks}
            else:
                break

        self.stopped_rocks |= rocks
        self.cache[self._simulation_hash()].append((self.rock_count, self.get_tower_size()))

        self.current_rock += 1
        self.current_rock %= 5

    def detect_cycles(self):
        cycles = None

        # check if a cycle was detected
        for value in self.cache.values():
            if len(value) > 1:
                # found a cycle
                cycles = value
                break

        if cycles is None:
            return -1, -1, -1, -1

        cycle_start, cycle_start_height = cycles[0]
        cycle_end, cycle_end_height = cycles[1]
        return (cycle_start,
                cycle_start_height,
                cycle_end - cycle_start,
                cycle_end_height - cycle_start_height)


def part1(data):
    simulation = Simulation(data)

    for _ in range(2022):
        simulation.simulate_falling_rock()
    return simulation.get_tower_size()


def part2(data):
    simulation = Simulation(data)

    # simulate sufficient many falling rocks to encounter a cycle
    heights = [0]
    for _ in range(2500):
        simulation.simulate_falling_rock()
        heights.append(simulation.get_tower_size())

    cycle_start, cycle_start_height, cycle_length, cycle_height = simulation.detect_cycles()
    assert cycle_start != -1, 'did not encounter a cycle'
    cycle_count, remainder = divmod(1_000_000_000_000 - cycle_start, cycle_length)

    # total height = height after cycle start + height of all cycles + remainder
    return cycle_start_height + cycle_count * cycle_height + (heights[cycle_start + remainder] - heights[cycle_start])


if __name__ == '__main__':
    print(f"Part 1: {part1(parse_input('day17.txt'))}")
    print(f"Part 2: {part2(parse_input('day17.txt'))}")
