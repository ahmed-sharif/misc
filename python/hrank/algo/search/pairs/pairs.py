# https://www.hackerrank.com/challenges/pairs
def pairs(items,k):
    # a contains array of numbers and k is the value of difference
    counts = {}
    exists = {}
    for i in items:
        exists[i] = True
        counts[i + k] = 1
    # print counts
    # print exists
    total = 0        
    for c in counts:
        if c in exists:
            total = total + 1

    
    return total
# Tail starts here
if __name__ == '__main__':
    a = map(int, raw_input().strip().split(" "))
    _a_size=a[0]
    _k=a[1]
    b = map(int, raw_input().strip().split(" "))
    print pairs(b,_k)
    
    
    
