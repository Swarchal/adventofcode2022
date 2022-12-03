import std/[os, strutils, sets]

func split(s: string): (string, string) =
  let midpoint = s.len div 2
  return (s[0 .. midpoint], s[midpoint..s.high])

func getDouble(s: string): char =
  let (x, y) = s.split
  for i in x:
    if y.contains(i):
      return i

func common(x: seq[string]): char =
  let
    y = x[1].toHashSet
    z = x[2].toHashSet
  for i in x[0].toHashSet:
    if y.contains(i) and z.contains(i):
      return i

func score(x: char): int =
  if x.isLowerAscii:
    return ord(x) - 96
  elif x.isUpperAscii:
    return ord(x) - 38

proc partA(x: seq[string]): int =
  for i in x:
    result += i.getDouble.score

proc partB(x: seq[string]): int =
  for i in countup(0, x.high-2, 3):
    var chunk = x[i..i+2]
    result += chunk.common.score

proc main() =
  let x = paramStr(1).readFile.splitWhitespace
  echo partA(x)
  echo partB(x)

when isMainModule:
  main()
