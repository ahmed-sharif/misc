"""
# testing find_corner
n = 4
mattrix = []
for x in range(n):
    mattrix.append([None]*n)
print mattrix

for i in range(n):
    for j in range(n):
        mattrix[i][j] = find_corner(n, (i, j))

for i in mattrix:
    for j in i:
        print "%-15s" % j,
    print
"""


# returns top-left, top-right, bot-left, bot-right
def find_corner(n, coordinate=(0,0)):
    row = coordinate[0]
    col = coordinate[1]

    if row < n/2:
        # top
        if col < n/2:
            # left
            return "TOP-LEFT"
        else:
            return "TOP-RIGHT"
    else:
        # bottom
        if col < n/2:
            # left
            return "BOTTOM-LEFT"
        else:
            return "BOTTOM-RIGHT"


def find_all_possible_position(n, coordinate, cn, results):
    #if start == coordinate:
    #    return []

    if cn >= n:
        return

    results.append(coordinate)
    row = coordinate[0]
    col = coordinate[1]

    corner = find_corner(n, coordinate)

    if corner == 'TOP-LEFT':
        new_row = n - 1 - row
        new_col = col
    elif corner == "BOTTOM-LEFT":
        new_row = row
        new_col = n - 1 - col
    elif corner == "BOTTOM-RIGHT":
        new_row = n - 1 - row
        new_col = col    
    elif corner == 'TOP-RIGHT':
        new_col = n - 1 - col
        new_row = row

    next_pos = (new_row, new_col)
    # return (coordinate) + find_all_possible_position(n, start, next_pos, cn + 1)
    find_all_possible_position(n, next_pos, cn + 1, results)


r = []
print find_all_possible_position(4, (0, 0), 0, r)
print r

r = []
print find_all_possible_position(4, (0, 1), 0, r)
print r


r = []
print find_all_possible_position(4, (1, 0), 0, r)
print r

r = []
print find_all_possible_position(4, (1, 1), 0, r)
print r
