import std/[os, strutils, algorithm, math]


proc main() =
  var
    x = paramStr(1).readFile.splitLines
    elves: seq[int]
    elf = 0
  for item in x:
    if item != "":
      elf += item.parseInt
    else:
      elves.add(elf)
      elf = 0
  echo max(elves)
  echo sum(sorted(elves, system.cmp)[^3..elves.high])


main()
