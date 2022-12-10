from typing import List, NamedTuple
from dataclasses import dataclass, astuple
from copy import copy
from math import sqrt, floor
import sys


@dataclass
class Coord:
    x: int
    y: int


class State(NamedTuple):
    head = Coord(0, 0)
    tail = Coord(0, 0)


class Instruction(NamedTuple):
    direc: str
    amnt: int


class Rope:
    def __init__(self):
        self.state = State
        self.head_positions = [self.state.head]
        self.tail_positions = [self.state.tail]

    def __str__(self):
        return str(self.state)

    def move(self, instr: Instruction) -> None:
        for _ in range(instr.amnt):
            # move head
            if instr.direc == "U":
                self.state.head.y += 1
            if instr.direc == "D":
                self.state.head.y -= 1
            if instr.direc == "L":
                self.state.head.x -= 1
            if instr.direc == "R":
                self.state.head.x += 1
            self.head_positions.append(self.state.head)
            if dist(self.state.head, self.state.tail) > 1:
                if instr.direc == "U":
                    self.state.tail.y = self.state.head.y - 1
                    self.state.tail.x = self.state.head.x
                if instr.direc == "D":
                    self.state.tail.y = self.state.head.y + 1
                    self.state.tail.x = self.state.head.x
                if instr.direc == "L":
                    self.state.tail.x = self.state.head.x + 1
                    self.state.tail.y = self.state.head.y
                if instr.direc == "R":
                    self.state.tail.x = self.state.head.x - 1
                    self.state.tail.y = self.state.head.y
            self.tail_positions.append(copy(self.state.tail))


def dist(u: Coord, v: Coord) -> int:
    return floor(sqrt(((u.x - v.x) ** 2) + ((u.y - v.y) ** 2)))


def read_input() -> List[Instruction]:
    output = []
    with open(sys.argv[1], "r") as f:
        for line in f.readlines():
            direc, amnt = line.strip().split()
            output.append(Instruction(direc, int(amnt)))
    return output


def main():
    x = read_input()
    r = Rope()
    for i in x:
        r.move(i)
    print(len(set([astuple(i) for i in r.tail_positions])))


if __name__ == "__main__":
    main()
