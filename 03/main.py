import sys
from typing import List, Tuple
from string import ascii_letters
from collections import defaultdict


score = defaultdict(int)
for i, j in enumerate(ascii_letters, 1):
    score[j] = i


def parse_input() -> List[str]:
    with open(sys.argv[1], "r") as f:
        return [i.strip() for i in f.readlines()]


def split(s: str) -> Tuple[str, str]:
    midpoint = len(s) // 2
    return (s[:midpoint], s[midpoint:])


def get_double(s: str):
    x, y = split(s)
    for i in x:
        if i in y:
            return i


def part_a() -> None:
    x = parse_input()
    print(sum(score[get_double(i)] for i in x))


def group(x: List[str]) -> List[List[str]]:
    idx = range(0, len(x) - 2, 3)
    return [x[i : i + 3] for i in idx]


def common(x: List[str]) -> str:
    for i in set(x[0]):
        if i in set(x[1]) and i in set(x[2]):
            return i
    raise RuntimeError("borked")


def part_b() -> None:
    x = group(parse_input())
    print(sum(score[common(i)] for i in x))


def main() -> None:
    part_a()
    part_b()


if __name__ == "__main__":
    main()
