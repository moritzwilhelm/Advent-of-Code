#!/usr/bin/env python3

def get_rules():
    rules = {}
    with open('input') as file:
        for line in file:
            line = line.strip()
            bag, content = line.split(' bags contain ')
            if content.startswith('no '):
                rules[bag] = {}
            else:
                rules[bag] = {inner_bag[2:inner_bag.find(' bag')]: int(inner_bag[:2]) for inner_bag in content.split(', ')}
    return rules


def part1(rules):
    shiny_gold_containing_bags = set()
    check_set = {'shiny gold'}
    while check_set:
        to_check = check_set.pop()
        for rule in rules:
            if to_check in rules[rule]:
                check_set.add(rule)
                shiny_gold_containing_bags.add(rule)
    return len(shiny_gold_containing_bags)


def get_inner_bag_count(rules, bag):
    if not rules[bag]:
        return 0
    else:
        return sum(rules[bag][inner_bag] + rules[bag][inner_bag] * get_inner_bag_count(rules, inner_bag) for inner_bag in rules[bag])


def part2(rules):
    return get_inner_bag_count(rules, 'shiny gold')


def main():
    rules = get_rules()
    print("Part 1:", part1(rules))
    print("Part 2:", part2(rules))


if __name__ == '__main__':
    main()
