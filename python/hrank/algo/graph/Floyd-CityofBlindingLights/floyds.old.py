#!/export/apps/python/3.5/bin/python3

# requires python 3
import math

raw_input = input
n, m = map(int, raw_input().strip().split())

vertexes = [x for x in range(1, n + 1)]

distance = []


# set distance[i][i] = 0 and infinity for every other position
for i in range(n):
    t = [math.inf for _ in range(n)]
    distance.append(t)
    distance[i][i] = 0

# populate distance matrics
for _ in range(m):
    u, v, r = map(int, raw_input().strip().split())
    distance[u - 1][v - 1] = r

# run floyd warshall algorithm
for k in range(n):
    for i in range(n):
        for j in range(n):
            if distance[i][k] + distance[k][j] < distance[i][j]:
                distance[i][j] = distance[i][k] + distance[k][j]


total_queries = int(raw_input().strip())
for _ in range(total_queries):
    u, v = map(int, raw_input().strip().split())
    result = distance[u - 1][v - 1]
    if result == math.inf:
        print (-1)
    else:
        print (result)

