
"""
5   4   3
4   3   5
"""


def rotate_list(s_list, s_index, count = 3):
    start_item = s_list[s_index]
    for i in range(s_index + 1, s_index + 1 + count - 1):
        s_list[i - 1] = s_list[i]
    s_list[s_index + count - 1] = start_item
    print s_list




sample = [1,   6,   5,   2,   4,   3]
print sample
for i in range(3):
    rotate_list(sample, 0)
