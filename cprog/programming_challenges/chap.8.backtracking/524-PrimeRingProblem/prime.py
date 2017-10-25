
primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]


def construct_candidates(a, k, n):
    if k == 1:
        return [1]
    else:
        in_perms = [False for _ in range(n+1)]
        for i in range(1, k):
            in_perms[a[i]] = True

        candidates = []
        
        for i in range(2, n + 1):
            if not in_perms[i]:
                if n != k:
                    if a[k-2] + i in primes:
                        candidates.append(i)
                else:
                    if a[0] + i in primes and  a[k-2] + i in primes:
                        candidates.append(i)
        
            
        return candidates


def backtrack(a, k, n):
    if n == k:
        print a
    else:
        k = k + 1
        candidates = construct_candidates(a, k, n)
        # print k, candidates, a
        for can in candidates:
            a[k-1] = can
            backtrack(a, k, n)
            a[k-1] = 0

#n = 6
#a = [0 for _ in range(n)]
#backtrack(a, 0, n)

n = 8
a = [0 for _ in range(n)]
backtrack(a, 0, n)
