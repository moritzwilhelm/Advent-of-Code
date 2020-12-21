#!/usr/bin/env python3
from collections import defaultdict


def parse_input():
    foods = []
    with open('input') as file:
        for line in file:
            a, b = line.strip().split('(contains ')
            ingredients = set(a.split())
            allergens = set(b[:-1].strip().split(', '))
            foods.append([ingredients, allergens])
    return foods


def get_allergen_mapping(foods):
    contained_in = {}
    for ingredients, allergens in foods:
        for allergen in allergens:
            if allergen in contained_in:
                contained_in[allergen] = contained_in[allergen].intersection(ingredients)
            else:
                contained_in[allergen] = ingredients

    while any(len(contained_in[allergen]) > 1 for allergen in contained_in):
        for allergen in contained_in:
            if len(contained_in[allergen]) == 1:
                for other in contained_in:
                    if other != allergen:
                        contained_in[other] = contained_in[other] - contained_in[allergen]

    return {allergen: contained_in[allergen].pop() for allergen in contained_in}


def part1(foods, contained_in):
    appearances = defaultdict(int)
    for ingredients, _ in foods:
        for ingredient in ingredients:
            if ingredient not in contained_in.values():
                appearances[ingredient] += 1
    return sum(appearances.values())


def part2(contained_in):
    return ','.join(ingredient for _, ingredient in sorted(contained_in.items()))


def main():
    foods = parse_input()
    contained_in = get_allergen_mapping(foods)
    print("Part 1:", part1(foods, contained_in))
    print("Part 2:", part2(contained_in))


if __name__ == '__main__':
    main()
