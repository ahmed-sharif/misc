

k = [2, 3, 7]
n = 12

result = [0 for _ in range(n+1)]

result[0] = 1

for i in range(n + 1):
    print i
    for j in k:
        if i >= j:
            print "--",j
            result[i] += result[i - j]
    print result[:i+1]
print result
