


fd = open("example_file1")
lines = []
for line in fd:
  lines.append(line.split())


for i in range(len(lines[0])):
  for j in range(len(lines)):
    print lines[j][i],
  print
