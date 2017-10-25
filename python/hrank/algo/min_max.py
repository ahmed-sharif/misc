


def manual(start, end):
    res = []
    for i in range(start, end + 1):
        s = str(i)
        for ind in range(1, len(s)-1):
            if s[ind] > s[ind - 1] and s[ind] > s[ind+1]:
                print s
                res.append(s)

    for i in range(start, end + 1):
        s = str(i)
        for ind in range(1, len(s)-1):
            if s[ind] < s[ind - 1] and s[ind] < s[ind + 1]:
                print s
                res.append(s)

    return res


def sum_n(n):
    return (n * (n + 1)) / 2


start = 100
end = 200
"""

"""
def calc(s):
    max_digit_count = sum_n(9) - sum_n(s)

    max_digit_count += sum_n(9) - sum_n(9 - s)

    return max_digit_count

def find_total(start=100, end=999):
    s = start / 100
    e = end / 100
    


    r = len(manual(200, 299))
    print "manual", r
    print "auto", calc(s + 1)

    r = len(manual(300, 399))
    print "manual", r
    print "auto", calc(s + 2)

print find_total()




