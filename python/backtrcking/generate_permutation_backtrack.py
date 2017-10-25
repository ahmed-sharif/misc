


items = ['1', '2', '3', '4']

def is_valid_solution(k, n):
    return k == n


def process_solution(a, k, n):
    # print a
    for i, val in enumerate(a):
        print items[a[i]],
    print

def construct_candidates(a, k , n):
    in_perms = [False for _ in range(n)]
    for i in range(k-1):
        in_perms[a[i]] = True

    candidates = [i for i in range(n) if in_perms[i] == False]
    return len(candidates), candidates


def backtrack(a, k, n):
    if(is_valid_solution(k, n)):
        process_solution(a, k, n)
    else:
        k = k + 1
        total_candidates, candidates = construct_candidates(a, k, n)
        for i in range(total_candidates):
            a[k-1] = candidates[i]
            backtrack(a, k, n)


a = [0,1,2, 3]
a = [None, None, None, None]
backtrack(a, 0, 4)




