#!/export/apps/python/3.5/bin/python3
import array
raw_input = input
n, m = map(int, raw_input().strip().split())

# vertexes = [x for x in range(1, n + 1)]

distance = []

numpyinf = 999999

# set distance[i][i] = 0 and infinity for every other position
for i in range(n):
    t = [numpyinf for _ in range(n)]
    a = array.array('i', t)
    distance.append(a)
    distance[i][i] = 0

# populate distance matrics
for _ in range(m):
    u, v, r = raw_input().strip().split()
    u, v, r = int(u), int(v), int(r)
    distance[u - 1][v - 1] = r

# run floyd warshall algorithm
for k in range(n):
    tempk = distance[k]
    for i in range(n):

        tempi = distance[i]
        #if tempi[k] == numpyinf:
        #    continue
        for j in range(n):
            #if tempk[j] == numpyinf:
            #    continue
            if tempi[k] + tempk[j] < tempi[j]:
                # distance[i][j] = tempi[k] + tempk[j]
                tempi[j] = tempi[k] + tempk[j]

output = []
total_queries = int(raw_input().strip())
for _ in range(total_queries):
    u, v = raw_input().strip().split()
    u, v = int(u), int(v)
    result = distance[u - 1][v - 1]
    if result == numpyinf:
        # print (-1)
        output.append("-1")
    else:
        # print (result)
        output.append(str(result))
print ("\n".join(output))

