



inp = [0 , 1,  2,  5,  3,  7,  8,  6,  4]

inp = [0, 2, 1, 5, 3, 4]
"""
swp = 0
for i in range(len(inp)):
  for j in range(len(inp) - i-1):
    if inp[j] > inp[j+1]:
      swp += 1
      t = inp[j]
      inp[j] = inp[j+1]
      inp[j+1] = t

# print inp, swp
"""
total = 0
for i in range(1, len(inp)):
    if inp[i] < i:
        #temp = inp[:i]
        ##tt = [1 for x in temp if x > inp[i]]
        #print tt
        total += sum([1 for x in inp[1:i] if x > inp[i]])
print total