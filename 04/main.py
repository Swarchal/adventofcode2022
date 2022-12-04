from typing import Tuple, List
import sys


def range_incl(start: int, stop: int) -> range:
    return range(start, stop + 1)


def parse_line(line: str) -> Tuple[range, range]:
    return tuple(range_incl(*map(int, i.split("-"))) for i in line.split(","))


def read_input() -> List[Tuple[range, range]]:
    with open(sys.argv[1], "r") as f:
        return list(map(parse_line, f.readlines()))


def contains(x: range, y: range) -> bool:
    xset, yset = set(x), set(y)
    return all(i in yset for i in xset) or all(i in xset for i in yset)


def overlaps(x: range, y: range) -> bool:
    return any(set(x) & set(y))


def main():
    x = read_input()
    print(sum(contains(*pair) for pair in x))
    print(sum(overlaps(*pair) for pair in x))


if __name__ == "__main__":
    main()
