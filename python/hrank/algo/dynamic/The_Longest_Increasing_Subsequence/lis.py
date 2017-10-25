# https://www.hackerrank.com/challenges/longest-increasing-subsequent
def compute_lis(a):
    n = len(a)
    lis = [1 for _ in range(n)]
    for i in range(1, n):
        for j in range(i):
            if a[i] > a[j]:
                lis[i] = max(lis[i], lis[j] + 1)
    return max(lis)

a = []
n = int(raw_input().strip())

for _ in range(n):
    a.append(int(raw_input().strip()))

    
print compute_lis(a)
