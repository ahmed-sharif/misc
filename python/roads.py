


def total_max(vertexes):
    return vertexes


vertexes = []
parents = []

n, m = raw_input().strip().split()
n = int(n)

for _ in range(n + 1):
    vertexes.append([None] * (n + 1))
    parents.append([None] * (n + 1))

for i in range(n + 1):
    vertexes[i][i] = 0

m = int(m)

for _ in range(m):
    a, b, c = raw_input().strip().split()
    a = int(a)
    b = int(b)
    c = int(c)

    vertexes[a][b] = pow(2, c)
    vertexes[b][a] = pow(2, c)


r=  total_max(vertexes)

for i in r:
    print i