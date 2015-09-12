place = 0 # 0) outside, 1) header, 2) body
pivot = -1
table = {}
file = open("/usr/share/PathDescriptions.md")
for line in file:
  if line[0] == '-':
    pivot = line.find(" -")+1
    if place == 2:
      place = 0
    else:
      place = place+1
  else:
    if place == 2:
      table[line[0:pivot].strip()] = line[pivot:].strip()

print(table)
