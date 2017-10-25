

from collections import deque

"""
s="1234"
d="8765"

s = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]
"""
    
def find_uniq(first, second):
    uniq_items = set()
    l1 = deque(first)
    ano = list(second)
    ano.reverse()
    l1.extend(ano)

    for i in range(len(l1)):
        # print list(l1)
        uniq_items.add(''.join(l1))
        l1.rotate()

    l2 = deque(second)
    ano = list(first)
    ano.reverse()
    l2.extend(ano)


    for i in range(len(l2)):
        # print list(l2)
        uniq_items.add(''.join(l2))
        l2.rotate()

    s = [list(first), list(second)]

    for k in range(2):
        output = []
        start = k
        for i in range(len(s[0])):
            if start == 0:
                output.append(s[0][i])
                output.append(s[1][i])
                start = 1
            else:
                output.append(s[1][i])
                output.append(s[0][i])
                start = 0
        # print output
        uniq_items.add(''.join(output))

        output = []
        start = k
        for i in range(len(s[0])-1, -1, -1):
            if start == 0:
                output.append(s[0][i])
                output.append(s[1][i])
                start = 1
            else:
                output.append(s[1][i])
                output.append(s[0][i])
                start = 0
        # print output        
        uniq_items.add(''.join(output))

    return uniq_items

"""
# print "a", "a"
r = find_uniq("a", "a")

print len(r)

print "dab", "abd"
r = find_uniq("dab", "abd")

print len(r)


print "ababa", "babab"
r = find_uniq("ababa", "babab")
print len(r)


#for i in r:
#    print i
"""

test_cases = int(raw_input().strip())
for _ in range(test_cases):
    asdf = raw_input().strip()

    first = raw_input().strip()
    second = raw_input().strip()
    print len(find_uniq(first, second))


