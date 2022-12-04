import std/[os, strutils, sets, sequtils, strscans]

func makeSet(start: int, stop:int): HashSet[int] =
  return countUp(start, stop).toSeq.toHashSet

func parse(line: string): (HashSet[int], HashSet[int]) =
  var a, b, x, y: int
  if line.scanf("$i-$i,$i-$i", a, b, x, y):
    return (makeSet(a, b), makeSet(x, y))

proc readInput(): seq[(HashSet[int], HashSet[int])] =
  return paramStr(1).readFile.splitWhitespace.map(parse)

func within(x: HashSet[int], y: HashSet[int]): int =
  return (if x < y or y < x: 1 else: 0)

func overlaps(x: HashSet[int], y: HashSet[int]): int =
  return (if len(x * y) > 0: 1 else: 0)

proc partA(input: seq[(HashSet[int], HashSet[int])]): int =
  for (x, y) in input:
    result += x.within y

proc partB(input: seq[(HashSet[int], HashSet[int])]): int =
  for (x, y) in input:
    result += x.overlaps y

when isMainModule:
  let input = readInput()
  echo partA(input)
  echo partB(input)

