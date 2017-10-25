"""
1  12 13 24 32 
7  18 19 10 43
11 11 11 11 55
13 14 15 16 67
19 20 21 22 43




1  2  3  4
7  8  9  10
13 14 15 16
19 20 21 22
25 26 27 28
"""

def _find_pos(i, j, row, col, t):
    ci = i
    cj = j
    for _ in range(t):
        if cj == col - i - 1:
            if ci == row - i -1:
                cj -= 1
            else:
                ci += 1
        elif ci == 0:
            if cj != col - i - 1:
                cj += 1
        elif cj == 0:
            if ci != 0:
                ci -= 1
        elif ci == row - 1 - j:
            ci -= 1            

        else:
            if ci == cj:
                
                cj += 1
            else:
                ci -= 1
    return (ci, cj)

def find_pos(i, j, row, col, t):


input =  [
  [1,  2,  3,  4,  5,  6],
  [7,  8,  9,  10, 11, 12],
  [13, 14, 15, 16, 17, 18],
  [19, 20, 21, 22, 23, 24],
  [25, 26, 27, 28, 29, 30],
]

for i in range(len(input)):
    for j in range(len(input[0])):
        r,c = find_pos(i, j, 5, 4, 1)
        print i,j,
        print "=",
        print r,c
        print input[r][c]
    print



