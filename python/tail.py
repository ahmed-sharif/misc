

import sys


# print sys.argv[0]

fd = open(sys.argv[1])

lines = [None] * 10
i = 0
for line in fd:
  lines[i] = line
  i += 1
  if i == 10:
    i = 0


for l in range(i, 10):
  if lines[l]:
    print lines[l].strip()

for l in range(0, i):
  if lines[l]:
    print lines[l].strip()
