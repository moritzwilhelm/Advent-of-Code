#!/usr/bin/env python3
from collections import deque


def parse_input():
    cups = deque()
    with open('input') as file:
        for value in file.readline().strip():
            cups.append(int(value))
    return cups


def play_game(cups, moves=100):
    max_cup = max(cups)
    for _ in range(moves):
        current = cups.popleft()
        pick_up = [cups.popleft(), cups.popleft(), cups.popleft()]

        destination = current - 1 or max_cup
        while destination in pick_up:
            if destination == 1:
                destination = max_cup
            else:
                destination -= 1

        new_cups = deque()
        while (cup := cups.popleft()) != destination:
            new_cups.append(cup)
        new_cups.append(cup)

        new_cups.extend(pick_up)
        new_cups.extend(cups)
        new_cups.append(current)
        cups = new_cups

    for _ in range(cups.index(1) + 1):
        cups.rotate(-1)

    return cups


def part1(cups):
    cups = play_game(cups)
    return ''.join(str(cups.popleft()) for _ in range(len(cups) - 1))


class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def __repr__(self):
        return f"Node({self.value})"


class LinkedList:
    def __init__(self):
        self.nodes = {}
        self.head = None
        self.tail = None

    def __len__(self):
        return len(self.nodes)

    def __repr__(self):
        res = []
        current = self.head
        while current != None:
            res.append(current)
            current = current.next
        return res.__repr__()

    def append(self, value):
        node = Node(value)
        if self.head:
            node.prev = self.tail
            self.tail.next = node
        else:
            self.head = node
        self.tail = node
        self.nodes[value] = node

    def get(self, value):
        return self.nodes[value]

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.nodes[node.value]

    def popleft(self):
        old_head_value = self.head.value
        self.head = self.head.next
        self.head.prev = None
        del self.nodes[old_head_value]
        return old_head_value

    def pop(self):
        old_tail_value = self.tail.value
        self.tail = self.tail.prev
        self.tail.next = None
        del self.nodes[old_tail_value]
        return old_tail_value

    def insert_after(self, node, iterable):
        for value in iterable:
            new = Node(value, node, node.next)
            node.next = new
            self.nodes[value] = new
            if self.tail == node:
                self.tail = new
            node = new

    def rotate_left(self):
        old_head = self.head
        self.head = old_head.next
        old_head.next = None
        old_head.prev = self.tail

        old_tail = self.tail
        old_tail.next = old_head

        self.tail = old_head


def play_game_LinkedList(cups, moves=10000000, max_cup=1000000):
    linked_cups = LinkedList()
    for cup in cups:
        linked_cups.append(cup)
    for i in range(max(cups) + 1, max_cup + 1):
        linked_cups.append(i)
    cups = linked_cups

    for _ in range(moves):
        current = cups.popleft()
        pick_up = [cups.popleft(), cups.popleft(), cups.popleft()]

        destination = current - 1 or max_cup
        while destination in pick_up:
            if destination == 1:
                destination = max_cup
            else:
                destination -= 1

        dest_node = cups.get(destination)
        cups.insert_after(dest_node, pick_up)
        cups.append(current)

    while cups.head.value != 1:
        cups.rotate_left()
    cups.rotate_left()

    return cups


def part2(cups):
    linked_cups = play_game_LinkedList(cups)
    first = linked_cups.popleft()
    second = linked_cups.popleft()
    return first * second


def main():
    cups = parse_input()
    print("Part 1:", part1(cups.copy()))
    print("Part 2:", part2(cups))


if __name__ == '__main__':
    main()
