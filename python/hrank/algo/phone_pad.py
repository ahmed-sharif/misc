items = [
[],
[],
['a', 'b', 'c'],
['d', 'e', 'f'],
['g', 'h', 'i'],
['j', 'k', 'l'],
['m', 'n', 'o'],
['p', 'q', 'r', 's'],
['t', 'u', 'v'],
['w', 'x', 'y', 'z'],
]


inputs = [2,3,4]
import sys
    
def comb(A, B):
    result = []
    for i in A:
        for j in B:
            result.append(i + j)
    return result


t1 = comb(items[2], items[3])
t2 = comb(t1, items[4])
import pprint
# pprint.pprint(t2)

a = "asdfasdfasdfasdfasdfadfdasfasdf"
b = "asdfasdfasdfasdfasdfadfdasfasdf"
c = "asdfasdfasdfasdfasdfadfdasfasdf"

# inps = [items[2], items[3], items[4]]
inps = [a, b, c, a, b] #, c, a, b, c]
r = reduce(comb, inps)

# pprint.pprint(r)
# assert t2 == r



