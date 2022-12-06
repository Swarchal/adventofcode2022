import std/[os, strutils, sets]

let input = paramStr(1).readFile()
var marker_len = paramStr(2).parseInt
for i in 0 .. input.high-(marker_len+1):
  let x = input[i..i+(marker_len-1)]
  if x.toHashSet.len == marker_len:
    echo i + marker_len
    break
