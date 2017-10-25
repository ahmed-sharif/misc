#!/export/apps/python/3.5/bin/python3



import math
import heapq
def disktra():
    vertexes = [1, 2, 3, 4]
    edges = {
        1: [(2, 24), (4, 20), (3, 3)],
        2: [(1, 24)],
        3: [(1, 3), (4, 12)],
        4: [(1, 20), (3, 12)]
    }
    distance = {}
    parents = {}
    source = 1
    for v in vertexes:
        distance[v] = math.inf
        parents[v] = None
    distance[source] = 0

    Q = distance.values()
    heapq.heapify(Q)

    while(Q):
        u = heapq.heappop(Q)
        
    


disktra()
