def answer(meetings):
  meetings = list(sorted(set(meetings), lambda t: t[1]))
  counter = 0
  last = meetings[0]
  for m in meetings[1:]:
    if m[0] >= last[1]:
      counter += 1
      last = m
  return counter
