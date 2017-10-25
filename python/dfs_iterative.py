dds = {0: 'a', 1:'b', 2:'c', 3: 'd', 4: 'e', 5:'f', 6:'g', 7:'h'}

def iter_dfs(G, s):
    S, Q = set(), []                            # Visited-set and queue
    Q.append(s)                                 # We plan on visiting s
    while Q:                                    # Planned nodes left?
        u = Q.pop()                             # Get one
        if u in S: 
            continue                     # Already visited? Skip it
        S.add(u)                                # We've visited it now
        Q.extend(G[u])                          # Schedule all neighbors
        print dds[u]


from collections import deque

def iter_bfs(G, s):
    Q = deque()
    Q.append(s)
    visited = set()

    while Q:
        item = Q.popleft()
        if item in visited:
            continue
        Q.extend(G[item])
        visited.add(item)
        print dds[item]


a, b, c, d, e, f, g, h = range(8)
G = [
    [b, c, d, e, f],    # a
    [c, e],             # b
    [d],                # c
    [e],                # d
    [f],                # e
    [c, g, h],          # f
    [f, h],             # g
    [f, g]              # h
]

iter_dfs(G, a)
print "-----------"
iter_bfs(G, a)



