import std/[os,strutils, sugar, strscans, sequtils, sets, algorithm]


type
  Register = seq[int]
  Screen = array[240, string]


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
  return cycles.map(x => x * r[x-1]).foldl(a + b)


proc draw_screen(r: Register): Screen =
  result.fill(".")
  const sprite_pos = [-1, 0, 1].toHashSet
  for idx, i in r:
    if (idx mod 40 - i) in sprite_pos:
      result[idx+1] = "#"


proc echo(s: Screen) =
  for idx, i in s:
    if idx mod 40 == 0: stdout.write "\n"
    else: stdout.write i


proc main() =
  let register = parseInput().get_register
  echo register.signal_strength()
  echo register.draw_screen()


when isMainModule:
  main()
