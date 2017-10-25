



import math
def coverPoints(X, Y):
    curr_pos = (X[0], Y[0])
    count = 0
    scount = 0
    for i in range(1, len(X)):
        next_pos = (X[i], Y[i])
        print curr_pos,next_pos
        dx = abs(curr_pos[0] - next_pos[0])
        dy = abs(curr_pos[1] - next_pos[1])

        # print math.sqrt(dx*dx + dy*dy)

        if dx < dy:
            print abs(dy) #+ abs(dy) - abs(dx)
        else:
            print abs(dx) # + abs(dy) - abs(dx)
        scount = scount + max(dy, dx)
        print "scount", scount    
            # print abs(dy) + abs(dx) - abs(dy)

        new_x = curr_pos[0]
        new_y = curr_pos[1]

        while True:
            # X axis
            if new_x == next_pos[0] and new_y == next_pos[1]:
                
                break
            print new_x, new_y

            if next_pos[0] > curr_pos[0]:
                new_x = curr_pos[0] + 1
            elif next_pos[0] < curr_pos[0]:
                new_x = curr_pos[0] - 1
            # Y axis    
            if next_pos[1] > curr_pos[1]:
                new_y = curr_pos[1] + 1
            elif next_pos[1] < curr_pos[1]:
                new_y = curr_pos[1] - 1
            count += 1
            curr_pos = (new_x, new_y)
            if new_x == next_pos[0] and new_y == next_pos[1]:
                
                break

        print count

    return count
    





X = [0, 1, 2, 1, 0]
Y = [0, 1, 2, 1, 0]

X = [ -7, -13 ]
Y = [ 1, -5 ]

X = [ -4,   1, -4, 8, -11, -12, -13, -3, -4, -4, -14, 7, -2, -2,  -5,  5,  -1,  0 ]
Y = [ -8, -15, -4, 3,  11,   8, -15,  4,  1,  7,   3, 9, -9, -9, -13, 10, -14, -8 ]
X = [ 4, 8, -7, -5, -13, 9, -7, 8 ]
Y = [ 4, -15, -10, -3, -13, 12, 8, -8 ]
print coverPoints(X, Y)
