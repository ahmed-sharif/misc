# https://www.hackerrank.com/challenges/is-fibo



from bisect import bisect_left


def generate_fib(fib_list, start, target):
    while True:
        res = fib_list[start - 1] + fib_list[start - 2]
        fib_list.append(res)
        if res == target:
            return True, start, res
        elif res > target:
            return False, start, res
        start += 1




is_fib_dict = {
    True: "IsFibo",
    False: "IsNotFibo"
}



fib_list = [0, 1]
start = 2
counted_max = 1


test_cases = int(raw_input().strip())
for _ in range(test_cases):
    t = int(raw_input().strip())
    if t <= counted_max:
        ndx = bisect_left(fib_list, t)

        if ndx < len(fib_list) and fib_list[ndx] == t:
            print "IsFibo"
        else:
            print "IsNotFibo"
    else:
        is_fib, start, counted_max = generate_fib(fib_list, start, t)
        print is_fib_dict[is_fib]
        start += 1
