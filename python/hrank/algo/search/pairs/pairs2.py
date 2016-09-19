# https://www.hackerrank.com/challenges/pairs
def pairs(items,k):
    total = 0
    for i in items:
        if i + k in items:
            total += 1
    return total

if __name__ == '__main__':
    a = map(int, raw_input().strip().split(" "))
    _a_size=a[0]
    _k=a[1]
    b = map(int, raw_input().strip().split(" "))
    print pairs(set(b),_k)
