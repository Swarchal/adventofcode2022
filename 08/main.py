from typing import List, Set
import sys
import math

N = 99
N_TEST = 99


class Tree:
    def __init__(self, id: int, height: int):
        self.id = id
        self.height = height

    def __str__(self):
        return str(self.height)

    def __rep__(self):
        return self.height

    def __hash__(self):
        return self.id


Grid = List[List[Tree]]


def parse_input() -> Grid:
    rows = []
    id = 1
    with open(sys.argv[1], "r") as f:
        lines = [i.strip() for i in f.readlines()]
    for i in lines:
        row = []
        for j in i:
            row.append(Tree(id=id, height=int(j)))
            id += 1
        rows.append(row)
    return rows


def rot90(x: Grid) -> None:
    """miss you numpy"""
    n = len(x[0])
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = x[i][j]
            x[i][j] = x[n - 1 - j][i]
            x[n - 1 - j][i] = x[n - 1 - i][n - 1 - j]
            x[n - 1 - i][n - 1 - j] = x[j][n - 1 - i]
            x[j][n - 1 - i] = temp


def get_visible(x: Grid) -> Set[Tree]:
    visible = set()
    for row in x:
        visible.add(row[0])  # edge tree
        cur_max = row[0].height
        for tree in row[1:]:
            if tree.height > cur_max:
                visible.add(tree)
                cur_max = tree.height
    return visible


def part_a(x: Grid) -> int:
    visible = set()
    for _ in range(4):
        visible |= get_visible(x)
        rot90(x)
    return len(visible)


def view(g: Grid, i: int, j: int):
    cols = list(zip(*g))
    above = cols[i][:j]
    left = g[j][:i]
    right = g[j][i + 1 :]
    below = cols[i][j + 1 :]
    return [above[::-1], left[::-1], right, below]


def score_view(start: Tree, direc: List[Tree]) -> int:
    score = 0
    for i in direc:
        score += 1
        if i.height >= start.height:
            break
    return score


def part_b(x: Grid) -> int:
    cur_max = 0
    for i in range(N_TEST):
        for j in range(N_TEST):
            views = view(x, i, j)
            start = x[i][j]
            score = math.prod([score_view(start, v) for v in views])
            if score > cur_max:
                cur_max = score
    return cur_max


def main() -> None:
    grid = parse_input()
    print(part_a(grid))
    print(part_b(grid))


if __name__ == "__main__":
    main()
