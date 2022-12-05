import sys
from collections import deque
from string import ascii_uppercase
from typing import NewType, List, Tuple, NamedTuple, Deque


State = NewType("State", List[List[Deque[str]]])


class Instruction(NamedTuple):
    n: int
    src: int
    dest: int


def parse_input() -> Tuple[State, List[Instruction]]:
    with open(sys.argv[1], "r") as f:
        top, bottom = f.read().split("\n\n")
    nums, *top = top.split("\n")[::-1]
    stacks = [deque() for _ in range(int(max(nums)))]
    for i in top:
        for idx, char in enumerate(i):
            if char in ascii_uppercase:
                stacks[idx // 4].append(char)
    instructions: List[Instruction] = []
    for i in bottom.strip().split("\n"):
        (_, n, _, src, _, dest) = i.split(" ")
        instr = Instruction(int(n), int(src) - 1, int(dest) - 1)
        instructions.append(instr)
    return stacks, instructions


class CargoStack:
    def __init__(self, state: State, crane=9000):
        self.state = state
        self.crane = crane

    @property
    def top(self) -> str:
        return "".join(i[-1] for i in self.state)

    def move(self, instr: Instruction) -> None:
        if self.crane == 9000:
            for _ in range(instr.n):
                self.state[instr.dest].append(self.state[instr.src].pop())
        if self.crane == 9001:
            buf = [self.state[instr.src].pop() for _ in range(instr.n)]
            for i in buf[::-1]:
                self.state[instr.dest].append(i)


def solve(crane=9000) -> str:
    state, instructions = parse_input()
    cargo = CargoStack(state, crane)
    for instr in instructions:
        cargo.move(instr)
    return cargo.top


if __name__ == "__main__":
    print(solve())
    print(solve(9001))
