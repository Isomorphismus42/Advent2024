# import numpy as np
# import re
from collections import OrderedDict
# import functools
# import math

with open("inputs/input_day20", "r") as file:
    grid = file.read().strip().splitlines()

grid = [list(char for char in line) for line in grid]
height = len(grid)
width = len(grid[0])

s = (0, 0)
e = (0, 0)
for r in range(height):
    for c in range(width):
        if grid[r][c] == "S":
            grid[r][c] = "."
            s = (r, c)
        elif grid[r][c] == "E":
            grid[r][c] = "."
            e = (r, c)


def regularPath():
    node = s
    steps = 0
    path = OrderedDict()
    path[s] = 0
    while node != e:
        row, col = node
        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_row, new_col = row + x, col + y
            if (new_row, new_col) not in path:
                if 0 <= new_row < height and 0 <= new_col < width:
                    if grid[new_row][new_col] == '.':
                        steps += 1
                        node = (new_row, new_col)
                        path[node] = steps
                        break
    return path, steps


def searchCheat(node, path, start_time, regular_time, max_time, max_cheat_time):
    found_cheats = 0
    for remaining_node, time in path.items():
        distance = abs(remaining_node[0] - node[0]) + abs(remaining_node[1] - node[1])
        if distance <= max_cheat_time:
            if regular_time - path[remaining_node] + start_time + distance <= max_time:
                found_cheats += 1
    return found_cheats


def part1():
    regular_path, regular_time = regularPath()
    max_time = regular_time - 100
    total_cheats = 0
    for i in range(len(regular_path)):
        node, start_time = regular_path.popitem(last=False)
        total_cheats += searchCheat(node, regular_path, start_time, regular_time, max_time, 2)
    return total_cheats


def part2():
    regular_path, regular_time = regularPath()
    max_time = regular_time - 100
    total_cheats = 0
    for i in range(len(regular_path)):
        node, start_time = regular_path.popitem(last=False)
        total_cheats += searchCheat(node, regular_path, start_time, regular_time, max_time, 20)
    return total_cheats


if __name__ == "__main__":
    print(part1())
