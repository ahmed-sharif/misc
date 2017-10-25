
import sys 


# recursive function to obtain the path as a string
def obtainPath(i, j):
    if dist[i][j] == float("inf"):
        return " no path to "
    if parent[i][j] == i:
        return " "
    else :
        return obtainPath(i, parent[i][j]) + str(parent[i][j]+1) + obtainPath(parent[i][j], j)

# no of vertices
n, m = raw_input().strip().split()
V = int(n)

# V = int(fil.readline().strip())
# array of shortest path distances 
dist = []
# array of shortest paths
parent = []

# no of edges
# E = int(fil.readline().strip())
E = int(m)

# initialize to infinity
for i in range (0, V):
    dist.append([])
    parent.append([])
    for j in range (0, V):
        dist[i].append(float("inf"))
        parent[i].append(0)


# read edges from input file and store
for i in range (0,E):
    t = raw_input().strip().split()
    x = int(t[0]) - 1
    y = int(t[1]) - 1
    w = pow(2, int(t[2]))
    dist[x][y] = w
    dist[y][x] = w
    parent[x][y] = x


# path from vertex to itself is set to 0
for i in range (0,V):
    dist[i][i] = 0



# initialize the path matrix
for i in range (0,V):
    for j in range (0,V):
        if dist[i][j] == float("inf"):
            parent[i][j] = 0
        else:
            parent[i][j] = i



# actual floyd warshall algorithm
for k in range(0,V):
    for i in range(0,V):
        for j in range(0,V):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                parent[i][j] = parent[k][j]
                

sums = 0
# display shortest paths 
for i in range (0,V):
    for j in range (i+1,V):
        # print "From :", i+1, " To :", j+1,
        sums += dist[i][j]
        # print " Distance :", dist[i][j]

# print bin(str(sums))
print bin(sums)[2:]