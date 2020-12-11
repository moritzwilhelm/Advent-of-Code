#!/usr/bin/env python3


def get_seat_layout():
    with open('input') as file:
        return [line.strip() for line in file]


def count_adjacent_occupied_seats(seat_layout, row, seat):
    occupied_seats = 0
    for i in range(max(0, row - 1), min(row + 2, len(seat_layout))):
        for j in range(max(0, seat - 1), min(seat + 2, len(seat_layout[row]))):
            if (i != row or j != seat) and seat_layout[i][j] == '#':
                occupied_seats += 1
    return occupied_seats


def count_visible_occupied_seats(seat_layout, row, seat):
    occupied_seats = 0
    # down
    for i in range(row + 1, len(seat_layout)):
        if seat_layout[i][seat] == 'L':
            break
        elif seat_layout[i][seat] == '#':
            occupied_seats += 1
            break
    # up
    for i in range(row - 1, -1, -1):
        if seat_layout[i][seat] == 'L':
            break
        elif seat_layout[i][seat] == '#':
            occupied_seats += 1
            break
    # right
    for i in range(seat + 1, len(seat_layout[row])):
        if seat_layout[row][i] == 'L':
            break
        elif seat_layout[row][i] == '#':
            occupied_seats += 1
            break

    # left
    for i in range(seat - 1, -1, -1):
        if seat_layout[row][i] == 'L':
            break
        elif seat_layout[row][i] == '#':
            occupied_seats += 1
            break

    # down + right
    for i, j in zip(range(row + 1, len(seat_layout)), range(seat + 1, len(seat_layout[row]))):
        if seat_layout[i][j] == 'L':
            break
        elif seat_layout[i][j] == '#':
            occupied_seats += 1
            break

    # down + left
    for i, j in zip(range(row + 1, len(seat_layout)), range(seat - 1, -1, -1)):
        if seat_layout[i][j] == 'L':
            break
        elif seat_layout[i][j] == '#':
            occupied_seats += 1
            break

    # up + right
    for i, j in zip(range(row - 1, -1, -1), range(seat + 1, len(seat_layout[row]))):
        if seat_layout[i][j] == 'L':
            break
        elif seat_layout[i][j] == '#':
            occupied_seats += 1
            break

    # up + left
    for i, j in zip(range(row - 1, -1, -1), range(seat - 1, -1, -1)):
        if seat_layout[i][j] == 'L':
            break
        elif seat_layout[i][j] == '#':
            occupied_seats += 1
            break

    return occupied_seats


def simulate_round_part(seat_layout, tolerance, count_visible=False):
    new_layout = []
    for row in range(len(seat_layout)):
        new_row = []
        for seat in range(len(seat_layout[row])):
            if not count_visible:
                occupied_seats = count_adjacent_occupied_seats(seat_layout, row, seat)
            else:
                occupied_seats = count_visible_occupied_seats(seat_layout, row, seat)
            if seat_layout[row][seat] == 'L' and occupied_seats == 0:
                new_row.append('#')
            elif seat_layout[row][seat] == '#' and occupied_seats > tolerance:
                new_row.append('L')
            else:
                new_row.append(seat_layout[row][seat])
        new_layout.append(new_row)
    return new_layout


def count_all_occupied_seats(seat_layout):
    count = 0
    for row in seat_layout:
        for seat in row:
            if seat == '#':
                count += 1
    return count


def part1(seat_layout):
    while (new_layout := simulate_round_part(seat_layout, 3)) != seat_layout:
        seat_layout = new_layout
    return count_all_occupied_seats(seat_layout)


def part2(seat_layout):
    while (new_layout := simulate_round_part(seat_layout, 4, True)) != seat_layout:
        seat_layout = new_layout
    return count_all_occupied_seats(seat_layout)


def main():
    seat_layout = get_seat_layout()
    print("Part 1:", part1(seat_layout))
    print("Part 2:", part2(seat_layout))


if __name__ == '__main__':
    main()
