import sys
from functools import cmp_to_key
from typing import List, Tuple

Packet = List[List | int]


def read_input(path: str) -> List[Tuple[Packet, Packet]]:
    with open(path, "r") as f:
        pairs = [i.strip() for i in f.read().split("\n\n")]
    return [tuple(eval(i) for i in p.split("\n")) for p in pairs if p != ""]


def listify(x: int | list) -> list:
    return x if isinstance(x, list) else [x]


def cmp(l: int | list, r: int | list) -> int:
    l, r = listify(l), listify(r)
    for i, j in zip(l, r):
        if isinstance(i, list) or isinstance(j, list):
            diff = cmp(i, j)
        else:
            diff = j - i
        if diff != 0:
            return diff
    return len(r) - len(l)


def part_a(data: List[Tuple[Packet, Packet]]) -> int:
    total = 0
    for idx, i in enumerate(data, 1):
        if cmp(*i) >= 0:
            total += idx
    return total


def part_b(data: List[Tuple[Packet, Packet]]) -> int:
    # flatten pairs, add dividor packets and sort
    dflat = sorted(list(sum(data, ())) + [[[2]], [[6]]], key=cmp_to_key(cmp))[::-1]
    packet_idx = []
    for idx, i in enumerate(dflat, 1):
        if i in ([[2]], [[6]]):
            packet_idx.append(idx)
    return packet_idx[0] * packet_idx[1]


def main():
    data = read_input(sys.argv[1])
    print(part_a(data))
    print(part_b(data))


if __name__ == "__main__":
    main()
