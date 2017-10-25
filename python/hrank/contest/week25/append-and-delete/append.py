

def common_prefix_length(s1, s2):
    # print s1, s2
    i = 0
    j = 0

    s1_l = len(s1)
    s2_l = len(s2)

    prefix_length = 0

    while i < s1_l and j < s2_l:
        if s1[i] != s2[j]:
            break
        prefix_length += 1
        i += 1
        j += 1

    return prefix_length


"""
hackerhappy
hackerrank
9

11

13


9 
12

21


abc
def


abcdd
adc

abc
abc

abc
abcddf


aba
aba
7


abc
def

min = 

ab
ac



"""


s = raw_input().strip()
t = raw_input().strip()
k = int(raw_input().strip())

# print common_prefix_length("hackerland", "hacke")


prefix_length = common_prefix_length(s, t)

unmatched_length = len(s) - prefix_length + len(t) - prefix_length


if unmatched_length == k:
    print "Yes"
else:
    if unmatched_length > k:
        print "No"
    else:
        extra_move = k - unmatched_length
        if extra_move % 2 == 0:
            print "Yes"
        else:
            full_removal = 2 * prefix_length + unmatched_length
            if k >= full_removal:
                print "Yes"
            else:
                print "No"

