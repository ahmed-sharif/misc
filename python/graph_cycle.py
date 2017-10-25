def iter_dfs(G, s):
    S = set()                            # Visited-set
    Q =  []                            #  queue
    Q.append(s)                                 # We plan on visiting s
    while Q:                                    # Planned nodes left?
        u = Q.pop()                             # Get one
        if u in S: 
            print "check", u
            continue                     # Already visited? Skip it
        S.add(u)                                # We've visited it now
        Q.extend(G[u])                          # Schedule all neighbors
        print u
    return S
from collections import deque


G = {}

G[1] = [3]
G[2] = [1]
G[3] = [6]
G[4] = [1]
G[5] = [7,8]
G[6] = [4]
G[7] = [9]
G[8] = [9]
G[9] = []


items = G.keys()
while True:
    s = iter_dfs(G, items[0])
    print s
    for i in s:
      if i in items:
          items.remove(i)
    if not items:
      break

