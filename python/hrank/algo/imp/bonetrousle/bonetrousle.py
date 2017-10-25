









def construct_candidates(a, k, n,target, option, current_sum):
    in_perms = [0 for _ in range(option + 1)]
    for i in range(k):
        in_perms[a[i]] = 1

    candidates = []
    for i in range(1, option + 1):
        if in_perms[i] == 1:
            continue
        proposed_sum = i + current_sum
        if k == n:
            if i < a[k-2]:
                continue
            if proposed_sum == target:
                candidates.append(i)
        else:
            if k != 1 and i < a[k-2]:
                continue
            if proposed_sum < target and (target - proposed_sum) >= i:
                candidates.append(i)

    return candidates


def backtrack(a, k, n, target, option, current_sum):
    # print a
    if n == k:
        # if is_valid_solution(a,n,k):
        # print "------", a
        return True
    else:
        k = k + 1
        candidates = construct_candidates(a, k, n, target, option, current_sum)
        for can in candidates:
            a[k - 1] = can
            solution_found = backtrack(a, k, n, target, option, current_sum + can)
            if solution_found:
                return True
            a[k - 1] = 0
    return False

"""
n = 3
target = 24
a = [0 for _ in range(n)]
option = 18
current_sum = 0
solution_found = backtrack(a, 0, n, target, option, current_sum)
if solution_found:
    print a
else:
    print -1
"""

test_cases = int(raw_input().strip())

for _ in range(test_cases):
    target, option, n = map(int, raw_input().strip().split())
    a = [0 for _ in range(n)]
    current_sum = 0
    solution_found = backtrack(a, 0, n, target, option, current_sum)
    if solution_found:
        a = map(str, a)
        print " ".join(a)
    else:
        print -1