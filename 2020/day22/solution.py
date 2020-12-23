#!/usr/bin/env python3
from collections import deque
from itertools import islice


def parse_input():
    player1 = deque()
    player2 = deque()
    with open('input') as file:
        p1, p2 = file.read().split('\n\n')
        for card in p1.split('\n')[1:]:
            player1.append(int(card))
        for card in p2.split('\n')[1:]:
            player2.append(int(card))
    return player1, player2


def compute_winner_score(winner):
    factor = 1
    result = 0
    while winner:
        result += factor * winner.pop()
        factor += 1
    return result


def part1(player1, player2):
    while player1 and player2:
        p1_card = player1.popleft()
        p2_card = player2.popleft()
        if p1_card > p2_card:
            player1.append(p1_card)
            player1.append(p2_card)
        else:
            player2.append(p2_card)
            player2.append(p1_card)

    return compute_winner_score(player1 or player2)


def recursive_combat(player1, player2, prev_rounds):
    while player1 and player2 and str((player1, player2)) not in prev_rounds:
        prev_rounds.add(str((player1, player2)))
        p1_card = player1.popleft()
        p2_card = player2.popleft()
        if p1_card <= len(player1) and p2_card <= len(player2):
            winner_id, _ = recursive_combat(deque(islice(player1, p1_card)), deque(islice(player2, p2_card)), set())
        else:
            winner_id = 1 if p1_card > p2_card else 2

        if winner_id == 1:
            player1.append(p1_card)
            player1.append(p2_card)
        else:
            player2.append(p2_card)
            player2.append(p1_card)
    return (1, player1) if player1 else (2, player2)


def part2(player1, player2):
    _, winner = recursive_combat(player1, player2, set())
    return compute_winner_score(winner)


def main():
    player1, player2 = parse_input()
    print("Part 1:", part1(player1.copy(), player2.copy()))
    print("Part 2:", part2(player1, player2))


if __name__ == '__main__':
    main()
