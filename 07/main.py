import sys
from collections import defaultdict

DIR_LIMIT = 100_000
FREE_SPACE = 30_000_000


def parse_input():
    with open(sys.argv[1], "r") as f:
        lines = [i.strip() for i in f.readlines()]
    counter = defaultdict(int)
    path = ()
    for line in lines:
        if line[0].isdigit():  # is file
            n_bytes = int(line.split()[0])
            for i in range(len(path)):
                counter[path[0 : i + 1]] += n_bytes
        elif line.startswith("$ cd"):
            dir = line.split()[-1]
            if dir == "..":
                path = path[:-1]
            else:
                path = path + (dir,)
    return counter


def sum_dirs(dirs, limit=DIR_LIMIT) -> int:
    return sum(i for i in dirs.values() if i <= limit)


def get_min_for_update(dirs, required_free=FREE_SPACE) -> int:
    result = sys.maxsize
    total_used = dirs[("/",)]
    for size in dirs.values():
        if (total_used - size) <= required_free and size < result:
            result = size
    return result


def main():
    data = parse_input()
    print(sum_dirs(data))
    print(get_min_for_update(data))


if __name__ == "__main__":
    main()
