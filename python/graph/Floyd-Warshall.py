#!/export/apps/python/3.5/bin/python3



import math
import heapq
import pprint
def floyd():
    vertexes = [1, 2, 3, 4]
    edges = {
        1: [(2, 5), (4, 24)],
        2: [(4, 6)],
        3: [(4, 4), (2, 7)],
        4: []
    }
    
    distance = [
        [0,         5,          math.inf,       24],
        [math.inf,  0,          math.inf,        6],
        [math.inf,  7,          0,               4],
        [math.inf,  math.inf,   math.inf,        0]
    ]

    n = len(vertexes)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distance[i][k] + distance[k][j] < distance[i][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]

    pprint.pprint(distance)

    print (distance[0][1])
    print (distance[2][0])
    print (distance[0][3])

floyd()
