



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

"""
G[1] = [3, 4] 
G[2] = [1] 
G[3] = [6] 
G[4] = [6]
G[5] = [7,8]
G[6] = [4]
G[7] = [9] 
G[8] = [9] 
G[9] = []
"""


WHITE = 1
GRAY = 2
BLACK = 3

terms = {1: "white", 2: "gray", 3: "black" }

res = {}
res["cycle"] = False

def dfs_visit(u, color):
    color[u] = GRAY
    #print "processing", u
    #print color
    for x in G[u]:
        #print "     neibor", x, "with color", terms[color[x]]

        if color[x] == WHITE:
            parent[x] = u
            dfs_visit(x, color)
        elif color[x] == GRAY:
            #print "cycle exist"
            res["cycle"] = True
            return True
    color[u] = BLACK
    return False


from collections import defaultdict
G = defaultdict(list)
test_cases = int(raw_input().strip())

for _ in range(test_cases):
    res["cycle"] = False
    G = defaultdict(list)
    inp = int(raw_input().strip())
    for _ in range(inp):
        places = raw_input().strip().split(",")
        for i in range(len(places) -1):
            G[places[i]].append(places[i + 1])
        if places[-1] not in G:
            G[places[-1]] = []


    #print G        

    color = {}
    parent = {}

    for i in G:
        color[i] = WHITE
        parent[i] = None



    for u in G:
        if color[u] == WHITE:
            r = dfs_visit(u, color)
            # print r
            if res["cycle"]:
                print "ORDER VIOLATION"
                break
    else:
        print "ORDER EXISTS"
