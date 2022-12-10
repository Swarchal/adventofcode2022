import sys
from typing import List


def read_input():
    with open(sys.argv[1], "r") as f:
        lines = [i.strip() for i in f.readlines()]
    return [0 if i == "noop" else int(i.split()[-1]) for i in lines]


def run_instructions(instructions: List[int]) -> List[int]:
    register = [1]
    for i in instructions:
        if i == 0:
            register.append(register[-1])
        else:
            register.extend([register[-1], register[-1] + i])
    return register


def signal_strength(register: List[int], cycles=[20, 60, 100, 140, 180, 220]) -> int:
    return sum(c * register[c - 1] for c in cycles)


def draw_screen(register: List[int]) -> str:
    screen = ["."] * 240
    sprite_pos = set([-1, 0, 1])
    for idx, x in enumerate(register):
        if idx % 40 - x in sprite_pos:
            screen[idx + 1] = "#"
    return "".join(screen)


def print_screen(screen: str) -> None:
    for idx, i in enumerate(screen):
        if idx % 40 == 0:
            print()
        else:
            print(i, end="")


def main():
    instructions = read_input()
    register = run_instructions(instructions)
    print(signal_strength(register))
    screen = draw_screen(register)
    print_screen(screen)


if __name__ == "__main__":
    main()
