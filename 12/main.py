import sys
import multiprocessing
from functools import partial
from typing import List, Tuple
from string import ascii_lowercase

CHAR_MAP = {char: idx for idx, char in enumerate(ascii_lowercase)}

Coord = Tuple[int, int]
Grid = List[List[int]]


def read_input(path: str) -> Tuple[Coord, Coord, Grid]:
    grid = []
    start, end = (-1, -1), (-1, -1)
    with open(path, "r") as f:
        lines = [i.strip() for i in f.readlines()]
    for y, line in enumerate(lines):
        row = []
        for x, char in enumerate(line):
            if char == "S":
                row.append(0)
                start = (y, x)
            elif char == "E":
                row.append(26)
                end = (y, x)
            else:
                row.append(CHAR_MAP[char])
        grid.append(row)
    return start, end, grid


def get_neighbours(g: Grid, c: Coord) -> List[Coord]:
    neighbours = []
    y_max, x_max = len(g) - 1, len(g[0]) - 1
    if c[0] < y_max:
        neighbours.append((c[0] + 1, c[1]))
    if c[0] > 0:
        neighbours.append((c[0] - 1, c[1]))
    if c[1] < x_max:
        neighbours.append((c[0], c[1] + 1))
    if c[1] > 0:
        neighbours.append((c[0], c[1] - 1))
    return neighbours


def bfs(start: Coord, end: Coord, grid: Grid) -> List[Coord] | None:
    visited = []
    queue = [(start, [])]
    while len(queue) > 0:
        node, path = queue.pop(0)
        path.append(node)
        if node not in visited:
            visited.append(node)
            if node == end:
                return path
            for neighbour in get_neighbours(grid, node):
                if neighbour not in visited:
                    y, x = neighbour
                    neighbour_height = grid[y][x]
                    current_height = grid[node[0]][node[1]]
                    if neighbour_height <= current_height + 1:
                        queue.append((neighbour, path[:]))
    return None


def part_a(start, end, g):
    path = bfs(start, end, g)
    if path:
        print(len(path) - 1)


def get_low_points(g: Grid) -> List[Coord]:
    low_points = []
    for y, row in enumerate(g):
        for x, col in enumerate(row):
            if col == 0:
                low_points.append((y, x))
    return low_points


def part_b(g, end):
    start_positions = get_low_points(g)
    with multiprocessing.Pool(16) as p:  # brute force
        paths = p.map(partial(bfs, grid=g, end=end), start_positions)
    dists = [len(i) - 1 for i in paths if i is not None]
    print(min(dists))


def main():
    start, end, g = read_input(sys.argv[1])
    part_a(start, end, g)
    part_b(g, end)


if __name__ == "__main__":
    main()
