
from collections import deque


def is_all_list_equal(l1, l2, l3):
    return is_all_equal(sum(l1), sum(l2), sum(l3))


def is_all_equal(n1, n2, n3):
    return n1 == n2 and n2 == n3

def max_list(l1, l2, l3):
    # print "input",l1,l2,l3
    max_sum = 0
    for l in [l1, l2, l3]:
        if sum(l) >= max_sum:
            max_sum = sum(l)
            rlist = l
    # print "output",rlist
    return rlist


n1, n2, n3 = map(int, raw_input().strip().split())

# stack_list = []
# stack_list = []

#for _ in xrange(3):
#   stack_list.append(deque(map(int, raw_input(),strip().split())))
stack_list1 = deque(map(int, raw_input().strip().split()))
stack_list2 = deque(map(int, raw_input().strip().split()))
stack_list3 = deque(map(int, raw_input().strip().split()))

while True:
    if is_all_list_equal(stack_list1, stack_list2, stack_list3):
        print sum(stack_list1)
        break
    # print stack_list1, stack_list2, stack_list3
    m_list = max_list(stack_list1, stack_list2, stack_list3)  
    # print m_list
    m_list.popleft()


