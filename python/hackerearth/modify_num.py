

result = {}

sum_dict = {}

def get_answer(n):
    repeated = set()
    if n == 1 or n == 4:
        return 'YES'
    
    original = n
    
    if n in result:
        return result[n]
    
    while True:

        if n in repeated:
            result[original] = 'NO'
            return 'NO'
        repeated.add(n)

        res = calculate_f(n)
        # print res
        
        if res == n:
            result[original] = 'NO'
            return 'NO'
        
        if res == 1 or res == 4:
            result[original] = 'YES'
            return 'YES'
        
        if res in result:
            return result[res]


        n = res


def calculate_f(n):
    res = sum_of_digits(n * n)
    return res


def sum_of_digits(n):
    
    if n in sum_dict:
        return sum_dict[n]
    
    sm = 0
    while n != 0:
        rem = n % 10
        sm += rem
        n = n / 10
    
    sum_dict[n] = sm
    return sm


t = int(raw_input().strip())


for _ in xrange(t):
    n = int(raw_input().strip())
    print get_answer(n)

