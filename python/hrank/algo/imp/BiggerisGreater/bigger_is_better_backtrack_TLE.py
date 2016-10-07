# https://www.hackerrank.com/challenges/bigger-is-greater
got_solution = [False]

def is_valid_solution(k, n):
    return k == n

def process_solution(a, k, n, original_items):
    # print a
    result = []
    for i, val in enumerate(a):
        result.append(original_items[a[i]])
    if "".join(original_items) != "".join(result):
        print "".join(result)
        got_solution[0] = True

def construct_candidates(a, k , n, items):
    in_perms = [False for _ in range(n)]
    for i in range(k-1):
        in_perms[a[i]] = True

    candidates = []
    # candidates = [i for i in range(n) if in_perms[i] == False]
    for i in range(n):
        if in_perms[i] == False:
            #
            temp = []
            for j in range(k-1):
                temp.append(items[a[j]])
            temp.append(items[i])
            if "".join(temp) < "".join(items[:k]):
                continue
            #
            candidates.append(i)
    candidates.sort(key=lambda y: items[y])
    # print candidates
    return len(candidates), candidates


def backtrack(a, k, n, original_items):
    # print got_solution
    if got_solution[0]:
        return

    if(is_valid_solution(k, n)):
        process_solution(a, k, n, original_items)
    else:
        k = k + 1
        total_candidates, candidates = construct_candidates(a, k, n, original_items)
        for i in range(total_candidates):
            a[k-1] = candidates[i]
            backtrack(a, k, n, original_items)


test_cases = int(raw_input().strip())
for i in range(test_cases):
    got_solution[0] = False
    items = list(raw_input().strip())

    a = [None for _ in range(len(items))]
    # items = ['b', 'b']
    backtrack(a, 0, len(items), items)

    if got_solution[0] == False:
        print "no answer"
    
