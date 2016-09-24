# https://www.hackerrank.com/challenges/bfsshortreach
# TODO: Need to use array instead of dict for colors, distances etc
from collections import deque


def bfs_distance(graph, s):
    vertexes = graph['V']
    adjacency_list = graph['AL']

    colors = {}
    distances = {}
    for v in vertexes:
        colors[v] = 'white'
        distances[v] = -1

    distances[s] = 0

    Q = deque()
    Q.append(s)
    while Q:
        u = Q.popleft()

        colors[u] = 'gray'
        for v in adjacency_list[u]:

            if colors[v] == 'white':
                colors[v] = 'gray'
                distances[v] = distances[u] + 6
                Q.append(v)

        colors[u] = 'black'
    return distances


q = int(raw_input().strip())

for _ in xrange(q):
    n, m = map(int, raw_input().strip().split())
    vertexes = [x for x in xrange(1, n + 1)]
    edges = {}
    for v in vertexes:
        edges[v] = set()
    for _ in xrange(m):
        u, v = map(int, raw_input().strip().split())
        edges[u].add(v)
        edges[v].add(u)
    s = int(raw_input().strip())

    distances = bfs_distance({'V': vertexes, 'AL': edges}, s)
    for v in vertexes:
        if s != v:
            print distances[v],
    print
