import sys


def main():
    with open(sys.argv[1], "r") as f:
        x = [i.strip() for i in f.readlines()]
    elves = []
    elf = 0
    for item in x:
        if item != "":
            elf += int(item)
        else:
            elves.append(elf)
            elf = 0
    print(max(elves))
    print(sum(sorted(elves)[-3:]))


main()
