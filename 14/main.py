import sys
import itertools
from typing import List, Tuple

SIZE = 1000
EMPTY = "."
ROCK = "#"
SAND = "o"


Coord = Tuple[int, int]
Block = List[Coord]


class Cave:
    def __init__(self, sand_point=(500, 0)):
        self.map = [[EMPTY for _ in range(SIZE)] for _ in range(SIZE)]
        self.sand_point = sand_point
        self.sand_units = 0
        self.overflowing = False

    def __str__(self) -> str:
        out = ""
        for i in self.map:
            for j in i:
                out += str(j)
            out += "\n"
        return out

    def add_blocks(self, blocks: List[Block]) -> None:
        for block in blocks:
            self.add_single_block(block)

    def add_single_block(self, block: Block) -> None:
        coords = []
        for i in range(len(block) - 1):
            u, v = block[i], block[i + 1]
            coords.extend(create_segment(u, v))
        for coord in coords:
            x, y = coord
            self.map[y][x] = ROCK

    def add_sand(self) -> None:
        sand_pos = self.sand_point
        while True:
            try:
                if self.map[self.sand_point[1]][self.sand_point[0]] == SAND:
                    self.overflowing = True
                    return
                elif self.map[sand_pos[1] + 1][sand_pos[0]] == EMPTY:
                    sand_pos = (sand_pos[0], sand_pos[1] + 1)  # move down
                elif self.map[sand_pos[1] + 1][sand_pos[0] - 1] == EMPTY:
                    sand_pos = (sand_pos[0] - 1, sand_pos[1] + 1)  # move down + left
                elif self.map[sand_pos[1] + 1][sand_pos[0] + 1] == EMPTY:
                    sand_pos = (sand_pos[0] + 1, sand_pos[1] + 1)  # move down + right
                else:
                    break
            except IndexError:  # into abyss
                self.overflowing = True
                return
        self.map[sand_pos[1]][sand_pos[0]] = SAND
        self.sand_units += 1

    @staticmethod
    def find_max_y(blocks: List[Block]) -> int:
        max_y = 0
        for block in blocks:
            for coord in block:
                if coord[1] > max_y:
                    max_y = coord[1]
        return max_y

    def add_floor(self, blocks: List[Block]) -> None:
        floor_y_pos = self.find_max_y(blocks) + 2
        for x in range(SIZE):
            self.map[floor_y_pos][x] = ROCK


def irange(start: int, stop: int) -> List[int]:
    # inclusive and bi-directional range
    if start < stop:
        return list(range(start, stop + 1))
    if start == stop:
        return [start]
    else:
        return list(range(start, stop - 1, -1))


def create_segment(u, v) -> List[Coord]:
    coords = itertools.product(irange(u[0], v[0]), irange(u[1], v[1]))
    return [tuple(i) for i in coords]


def parse_block(block: str) -> Block:
    return [tuple(map(int, i.split(","))) for i in block.split(" -> ")]


def parse_input(fpath: str) -> List[Block]:
    with open(fpath, "r") as f:
        blocks = [parse_block(i.strip()) for i in f.readlines()]
    return blocks


def part_a(blocks) -> int:
    cave = Cave()
    cave.add_blocks(blocks)
    while cave.overflowing is False:
        cave.add_sand()
    return cave.sand_units


def part_b(blocks) -> int:
    cave = Cave()
    cave.add_blocks(blocks)
    cave.add_floor(blocks)
    while cave.overflowing is False:
        cave.add_sand()
    return cave.sand_units


def main() -> None:
    blocks = parse_input(sys.argv[1])
    # blocks = [[(2, 1), (2, 3), (0, 3)], [(3, 5), (9, 5)]]
    print(part_a(blocks))
    print(part_b(blocks))


if __name__ == "__main__":
    main()
