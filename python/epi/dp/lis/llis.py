items = [ 5, 3, 4, 8, 6, 7, 1]

liss = [1 for _ in range(len(items))]
print items

for i in range(1, len(items)):
    for j in range(i):
        if items[i] >= items[j]:
            liss[i] = max(liss[j] + 1, liss[i])


print liss
