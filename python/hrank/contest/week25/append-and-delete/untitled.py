


"""
hackerhappy
hackerrank
9

abc
def


abcdd
adc


abc
abcddf

"""


#s = raw_input().strip()
#t = raw_input().strip()
#k = int(raw_input().strip())



def common_prefix_length(s1, s2):
    print s1, s2
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

print common_prefix_length("hackerhappy", "hackerrank")
print common_prefix_length("hacker", "hacker")
print common_prefix_length("abc", "abc")

print common_prefix_length("abc", "defg")

print common_prefix_length("defg", "avh")



print common_prefix_length("hacker", "hackerland")

print common_prefix_length("hackerland", "hacke")