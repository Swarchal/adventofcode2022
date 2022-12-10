import std/[os,strutils, sugar, strscans, sequtils, sets]


type
  Register = seq[int]
  Screen = string


proc parseInput(): seq[int] =
  var val: int
  for l in paramStr(1).readFile.splitLines:
    if l == "": continue
    if l.scanf("addx $i", val):
      result.add(val)
    else:
      result.add(0)


func get_register(instructions: seq[int]): Register =
  result.add(1)
  for i in instructions:
    if i == 0:
      result.add(result[^1])
    else:
      result.add(@[result[^1], result[^1] + i])


func signal_strength(r: Register, cycles=[20, 60, 100, 140, 180, 220]): int =
  return cycles.map(c => c * r[c-1]).foldl(a + b)


proc draw_screen(r: Register): string =
  result = "#"
  const sprite_pos = [-1, 0, 1].toHashSet
  for idx, i in r:
    if (idx mod 40 - i) in sprite_pos:
      result.add("#")
    else: result.add(".")


proc echo(s: Screen) =
  for idx, i in s:
    if idx mod 40 == 0: stdout.write "\n"
    else: stdout.write i


proc main() =
  let register = parseInput().get_register
  echo register.signal_strength
  echo register.draw_screen


when isMainModule:
  main()
