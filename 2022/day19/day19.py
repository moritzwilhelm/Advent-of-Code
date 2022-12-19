#!/usr/bin/env python3
import re
from collections import defaultdict
from functools import cache, reduce
from operator import mul

BLUEPRINT_REGEX = re.compile(
    r"Blueprint (\d+): Each ore robot costs (\d) ore. Each clay robot costs (\d) ore. Each obsidian robot costs (\d) ore and (\d+) clay. Each geode robot costs (\d) ore and (\d+) obsidian.")


def parse_input(filename):
    with open(filename) as file:
        return [tuple(map(int, BLUEPRINT_REGEX.match(line).groups())) for line in file]


def max_geodes(ore_robot_cost_ore,
               clay_robot_cost_ore,
               obsidian_robot_cost_ore,
               obsidian_robot_cost_clay,
               geode_robot_cost_ore,
               geode_robot_cost_obsidian,
               minutes_left=24):
    current_max = defaultdict(int)

    @cache
    def _max_geodes(ore=0,
                    clay=0,
                    obsidian=0,
                    geodes=0,
                    ore_robots=1,
                    clay_robots=0,
                    obsidian_robots=0,
                    geode_robots=0,
                    minutes_left=24):
        if minutes_left == 0:
            return geodes

        # update current max geode count
        current_max[minutes_left] = max(current_max[minutes_left], geodes)

        # check if current run can beat a previous run by building a geode robot each turn (if not -> abort)
        possible_geodes = geodes + sum(geode_robots + new_geode_robots for new_geode_robots in range(minutes_left - 1))
        if possible_geodes < current_max[minutes_left]:
            return -1

        # geode robot
        if ore >= geode_robot_cost_ore and obsidian >= geode_robot_cost_obsidian:
            return _max_geodes(
                (ore + ore_robots) - geode_robot_cost_ore,
                (clay + clay_robots),
                (obsidian + obsidian_robots) - geode_robot_cost_obsidian,
                (geodes + geode_robots),
                ore_robots,
                clay_robots,
                obsidian_robots,
                geode_robots + 1,
                minutes_left - 1,
            )

        # check if we will never be able to build a geode robot again (based on obsidian)
        possible_obsidian = obsidian + sum(
            obsidian_robots + new_obsidian_robots for new_obsidian_robots in range(minutes_left - 2))
        if possible_obsidian < geode_robot_cost_obsidian:
            return geodes + (geode_robots * minutes_left)

        # compute maximum of remaining (meaningful) options
        options = []

        # obsidian robot
        if ore >= obsidian_robot_cost_ore and clay >= obsidian_robot_cost_clay and obsidian_robots < geode_robot_cost_obsidian:
            options.append(
                _max_geodes(
                    (ore + ore_robots) - obsidian_robot_cost_ore,
                    (clay + clay_robots) - obsidian_robot_cost_clay,
                    (obsidian + obsidian_robots),
                    (geodes + geode_robots),
                    ore_robots,
                    clay_robots,
                    obsidian_robots + 1,
                    geode_robots,
                    minutes_left - 1
                ))

        # clay robot
        if ore >= clay_robot_cost_ore and clay_robots < obsidian_robot_cost_clay:
            options.append(
                _max_geodes(
                    (ore + ore_robots) - clay_robot_cost_ore,
                    (clay + clay_robots),
                    (obsidian + obsidian_robots),
                    (geodes + geode_robots),
                    ore_robots,
                    clay_robots + 1,
                    obsidian_robots,
                    geode_robots,
                    minutes_left - 1
                ))

        # ore robot
        if ore >= ore_robot_cost_ore and ore_robots < max(clay_robot_cost_ore, obsidian_robot_cost_ore,
                                                          geode_robot_cost_ore):
            options.append(
                _max_geodes(
                    (ore + ore_robots) - ore_robot_cost_ore,
                    (clay + clay_robots),
                    (obsidian + obsidian_robots),
                    (geodes + geode_robots),
                    ore_robots + 1,
                    clay_robots,
                    obsidian_robots,
                    geode_robots,
                    minutes_left - 1
                ))

        # no robot
        options.append(
            _max_geodes(
                (ore + ore_robots),
                (clay + clay_robots),
                (obsidian + obsidian_robots),
                (geodes + geode_robots),
                ore_robots,
                clay_robots,
                obsidian_robots,
                geode_robots,
                minutes_left - 1
            ))

        return max(options)

    return _max_geodes(minutes_left=minutes_left)


def compute_quality_number(blueprint_id, *recipes):
    return blueprint_id * max_geodes(*recipes)


def part1(data):
    return sum(compute_quality_number(*blueprint) for blueprint in data)


def part2(data):
    return reduce(mul, [max_geodes(*recipes, minutes_left=32) for _, *recipes in data[:3]])


if __name__ == '__main__':
    print(f"Part 1: {part1(parse_input('day19.txt'))}")
    print(f"Part 2: {part2(parse_input('day19.txt'))}")
