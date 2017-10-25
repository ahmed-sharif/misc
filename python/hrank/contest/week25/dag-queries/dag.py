n, m, q = map(int, raw_input().strip().split())

vertexes = set()
colors = {}
parents = {}

distances = {}

values_v = {}

edges = {}


def bfs():
    for v in vertexes:
        colors[v] = 'white'

    parents[source] = None
    distances[source] = 0

    for v in vertexes:
        if colors[v] == 'white':

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





for edge in xrange(m):
    u, v = map(int, raw_input().strip().split())
    vertexes.add(u)
    vertexes.add(v)

    if u in edges:
        edges[u].append(v)
    else:
        edges[u] = [v]


# ### BFS #####
            
