from typing import List, Tuple
import sys

LOSS = 0
DRAW = 3
WIN = 6

MAPPING = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
}

MAPPING_2 = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "loss",
    "Y": "draw",
    "Z": "win",
}

SCORE_DICT = {
    ("rock", "rock"): DRAW,
    ("paper", "paper"): DRAW,
    ("scissors", "scissors"): DRAW,
    ("rock", "paper"): WIN,
    ("paper", "scissors"): WIN,
    ("scissors", "rock"): WIN,
    ("rock", "scissors"): LOSS,
    ("paper", "rock"): LOSS,
    ("scissors", "paper"): LOSS,
}

GAME_DICT = {
    "rock": {"win": "paper", "draw": "rock", "loss": "scissors"},
    "paper": {"win": "scissors", "draw": "paper", "loss": "rock"},
    "scissors": {"win": "rock", "draw": "scissors", "loss": "paper"},
}

ITEM_DICT = {"rock": 1, "paper": 2, "scissors": 3}
OUTCOME_DICT = {"loss": LOSS, "draw": DRAW, "win": WIN}


def parse_input(mapper=MAPPING) -> List[Tuple]:
    output = []
    with open(sys.argv[1], "r") as f:
        for i in f.readlines():
            a, b = i.strip().split()
            output.append((mapper[a], mapper[b]))
    return output


def part_a(games: List[Tuple]) -> int:
    return sum(SCORE_DICT[i] + ITEM_DICT[i[1]] for i in games)


def part_b(games: List[Tuple]) -> int:
    return sum(ITEM_DICT[GAME_DICT[p][o]] + OUTCOME_DICT[o] for p, o in games)


def main():
    x_a = parse_input()
    x_b = parse_input(MAPPING_2)
    print(part_a(x_a))
    print(part_b(x_b))


if __name__ == "__main__":
    main()
