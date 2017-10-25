


# count the number of ways to traverse a 2d array
import pprint

def find_ways(n, m):
    ways = []
    for _ in range(n):
        ways.append([0 for _ in range(m)])

    for i in range(n):
        ways[i][m - 1] = 1

    for j in range(m):
        ways[n - 1][j] = 1


    for i in range(n - 2, -1, -1):
        for j in range(m - 2, -1, -1):
            ways[i][j] = ways[i + 1][j] + ways[i][j + 1]
    # pprint.pprint( ways)
    for i in range(n):
        for j in range(m):
            print "%3d " % ways[i][j],
        print
    return ways[0][0]


print find_ways(5, 5)




