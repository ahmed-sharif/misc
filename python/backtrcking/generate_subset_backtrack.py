


items = ['a', 'b', 'c']

def is_valid_solution(k, n):
    return k == n


def process_solution(a, k, n):
    # print a
    for i, val in enumerate(a):
        if val:
            print items[i],
    print


def construct_candidates(a, k , n):
    candidates = [True, False]
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


a = [0,1,2]
a = [None, None, None]
backtrack(a, 0, 3)




