

def footprint(s):
    print s
    indexes = [0 for _ in xrange(26)]
    for ch in s:
        indexes[ord(ch) - ord('a')] += 1
    footp = 0
    feed = 7
    for x in indexes:
        print 'footp = footp * feed + x  =', footp, ' * 7 + ', x, '=',footp * feed + x
        footp = footp * feed + x
    print footp    
    return footp



items = ["eat", "tea", "tan", "ate", "nat", "bat"]


for item in items:
    footprint(item)
