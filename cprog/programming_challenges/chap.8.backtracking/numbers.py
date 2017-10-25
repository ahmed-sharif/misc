
def construct_candidates(a, k, current, n):
    solutions = []
    total = n * 2

    for i in range(n*2):
        if i + current + 1 >= len(a):
            break
        if not a[i] and not a[i+current+1]:
            solutions.append((i, i+current+1))
    return len(solutions), solutions

def is_a_solution(a, k, n):
    return True

def process_solution(a, k, n):
    print a

def backtrack(a, k, current, n):
    # print a, k, current, n
    # if current ==0 and is_a_solution(a, k, n):
    if current ==0:
        process_solution(a, k , n)
    else:
        k = k + 1
        total_candidates, candidates = construct_candidates(a, k, current, n)
        for can in candidates:
            first = can[0]
            second = can[1]

            # save the current value
            t1 = a[first]
            t2 = a[second]
            
            a[first] = current
            a[second] = current


            backtrack(a, k, current -1, n)
            # restore the value
            a[first] = t1
            a[second] = t2

a = [None for _ in range(8)]

backtrack(a, 0, 4, 4)


a = [None for _ in range(14)]

backtrack(a, 0, 7, 7)
