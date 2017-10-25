


def is_a_solution(a, n):
    return a == n


def construct_candidates(a, k):
    candidates = [True, False]
    return candidates

def process_solution(a, k):
    for index, i in enumerate(a):
        if i:
            print index



def backtrack(a, k, n, solution):
    if is_a_solution(a, n):
        process_solution(a, k)
    else:
        k = k + 1
        candidates = construct_candidate(a, k)
        for can in candidates:
            a[k] = can
            backtrack(a, k, n, solution)



