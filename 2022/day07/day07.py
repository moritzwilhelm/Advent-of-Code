#!/usr/bin/env python3

class Node:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.files = {}
        self.dirs = set()

    def __iter__(self):
        yield self
        for dir in self.dirs:
            for sub_dir in dir:
                yield sub_dir

    def __repr__(self):
        representation = f"- {self.name} (dir)\n"

        for dir in sorted(self.dirs, key=lambda node: node.name):
            dir_representation = dir.__repr__().replace('\n', '\n ')
            representation += f" {dir_representation}\n"

        for file in sorted(self.files):
            representation += f" - {file} (file, size={self.files[file]})\n"

        return representation[:-1]

    def add_dir(self, name):
        child = Node(name, self)
        self.dirs.add(child)
        return child

    def add_file(self, name, size):
        self.files[name] = size

    def size(self):
        return sum(dir.size() for dir in self.dirs) + sum(self.files.values())


def parse_input(filename):
    with open(filename) as file:
        filesystem = Node(file.readline().strip().split()[-1])

        current_node = filesystem
        for line in file:
            if line.startswith('$ cd'):
                _, _, name = line.strip().split()
                if name != '..':
                    current_node = current_node.add_dir(name)
                else:
                    current_node = current_node.parent
            elif not line.startswith('$ ls') and not line.startswith('dir'):
                size, name = line.strip().split()
                current_node.add_file(name, int(size))

    return filesystem


def part1(data):
    return sum(size for dir in data if (size := dir.size()) <= 100000)


def part2(data):
    needed_space = data.size() - 40000000
    return min(size for dir in data if (size := dir.size()) >= needed_space)


if __name__ == '__main__':
    print(f"Part 1: {part1(parse_input('day07.txt'))}")
    print(f"Part 2: {part2(parse_input('day07.txt'))}")
