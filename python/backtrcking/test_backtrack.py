



def is_valid_solution(k, n):
    return k == n


def process_solution(a, k, n):
    # print a
    for i, val in enumerate(a):
        if val:
            print i,
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
            a[k] = candidates[i]
            backtrack(a, k, n)



a = [0,1,2,3]
backtrack(a, 0, 3)




