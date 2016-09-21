from pprint import pprint
from collections import deque

# example from coremen
vertexes = ['r', 's', 't', 'u', 'v', 'w', 'x', 'y']

edges = {}

edges['r'] = ['s', 'v']
edges['s'] = ['r', 'w']
edges['t'] = ['w', 'x', 'u']
edges['u'] = ['t', 'x', 'y']
edges['v'] = ['r']
edges['w'] = ['x', 't', 's']
edges['x'] = ['w', 'y', 'u', 't']
edges['y'] = ['x', 'u']


colors = {}
parents = {}

distances = {}

source = 's'

# ### BFS #####
for v in vertexes:
    colors[v] = 'white'

parents[source] = None
distances[source] = 0

Q = deque()
Q.append(source)

while Q:
    u = Q.popleft()
    colors[u] = 'gray'
    for v in edges[u]:
        if colors[v] == 'white':
            colors[v] = 'gray'
            parents[v] = u
            distances[v] = distances[u] + 1
            Q.append(v)
    colors[u] = 'black'
# ### END BFS #####

pprint(colors)
pprint(parents)
pprint(distances)
