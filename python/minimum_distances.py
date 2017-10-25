
from collections import defaultdict

A = [7, 1, 3, 4, 1, 7, 7]

# A = [7]



indexes = defaultdict(list)

for index, number  in enumerate(A):
    indexes[number].append(index)

multiple_number_list = []


distances = []
print indexes
for number, index in indexes.iteritems():
    if len(index) > 1:
        for i in range(1, len(index)):
            distances.append(abs(index[i] - index[i - 1]))

if distances:
    print min(distances)
else:
    print -1

