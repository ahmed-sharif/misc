N, M = raw_input().strip().split()
N, M = int(N), int(M)

vertexes = [n for n in xrange(1, N + 1)]
edges = {}

for v in vertexes:
    edges[v] = []

for _ in xrange(M):
    i, j = raw_input().strip().split()
    i, j = int(i), int(j)
    edges[i].append(j)
    edges[j].append(i)

G = {'V': vertexes, 'E': edges}

extended_dfs(G)
