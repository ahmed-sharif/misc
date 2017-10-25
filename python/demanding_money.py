import sys





N, E = raw_input().strip().split(' ')

N = int(N)
E = int(E)


visited = [0] * N
taken = [0] * N
edeges = [[None] * N for _ in range(N)]

edge_list = {}

vertexes = map(int,raw_input().strip().split(' '))

for i in range(E):
    x, y = map(int,raw_input().strip().split(' '))
    if x in edge_list:
        edge_list[x].append(y)
    else:
        edge_list[x] = [y]

    if y in edge_list:
        edge_list[y].append(x)
    else:
        edge_list[y] = [x]
    edeges[x - 1][y - 1] = 1
    edeges[y - 1][x - 1] = 1

print vertexes
# for i in edeges:
#    print i
print edge_list



def traverse(start, vertexes, edge_list, visited):
    # print vertexes[start]
    print start, visited
    print start
    visited[start] = 1
    for i in edge_list[start]:
        if visited[i] == 0:
            traverse(i, vertexes, edge_list, visited)

v_list = [i for i in range(1, N+1)]
visited = {}
for i in v_list:
    visited[i] = 0

traverse(1, v_list, edge_list, visited)
print "----"
