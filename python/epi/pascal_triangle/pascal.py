



a = [
    [0,0,0]
]


a = []
n = 5

for _ in range(n):
    a.append([0 for _ in range(n)])

for i in range(n):
    a[i][i] = 1
    a[i][0] = 1

for i in range(n):
    for j in range(1, i):
        a[i][j] = a[i-1][j-1] + a[i-1][j]


for i in a:
    print i



a = [0 for _ in range(n)]

a[0] = 1

for i in range(n):
    a[i] = 1
    for j in range(i-1, 0, -1):
        a[j] = a[j-1] + a[j] 


print "--------"
print a
