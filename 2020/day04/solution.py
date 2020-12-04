#!/usr/bin/env python3
from re import search


def parse_passports():
    passports = []
    with open('input') as file:
        passport = {}
        for line in file:
            line = line.strip()
            if line == '':
                passports.append(passport)
                passport = {}
            else:
                for field in line.split():
                    name, value = field.split(':')
                    passport[name] = value

    # no empty line at end of file
    passports.append(passport)

    return passports


def part1(passports):
    correct_passports = 0
    for passport in passports:
        if {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}.issubset(passport.keys()):
            correct_passports += 1
    return correct_passports


def part2(passports):
    correct_passports = 0
    for passport in passports:
        try:
            rule_byr = len(passport['byr']) == 4 and 1920 <= int(passport['byr']) <= 2002
            rule_iyr = len(passport['iyr']) == 4 and 2010 <= int(passport['iyr']) <= 2020
            rule_eyr = len(passport['eyr']) == 4 and 2020 <= int(passport['eyr']) <= 2030
            rule_hgt = passport['hgt'].endswith('cm') and 150 <= int(passport['hgt'][:-2]) <= 193 or \
                       passport['hgt'].endswith('in') and 59 <= int(passport['hgt'][:-2]) <= 76
            rule_hcl = search('^#[0-9a-f]{6}$', passport['hcl'])
            rule_ecl = passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
            rule_pid = search('^[0-9]{9}$', passport['pid'])

            if rule_byr and rule_iyr and rule_eyr and rule_hgt and rule_hcl and rule_ecl and rule_pid:
                correct_passports += 1
        except (KeyError, ValueError):
            pass
    return correct_passports


def main():
    passports = parse_passports()
    print("Part 1:", part1(passports))
    print("Part 2:", part2(passports))


if __name__ == '__main__':
    main()
