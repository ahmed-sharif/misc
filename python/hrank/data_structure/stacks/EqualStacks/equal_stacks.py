"""
https://www.hackerrank.com/challenges/equal-stacks

You have three stacks of cylinders where each cylinder has the same diameter,
but they may vary in height. You can change the height of a stack by removing and discarding
its topmost cylinder any number of times.

Find the maximum possible height of the stacks such that all of the stacks are exactly the same height. 
This means you must remove zero or more cylinders from the top of zero or more of the three stacks 
until they're all the same height, then print the height. The removals must be performed in such a way as to
maximize the height.
"""

from collections import deque

def is_all_sum_equal(smn1, smn2, smn3):
    return smn1 == smn2 and smn2 == smn3

def max_list(l1, l2, l3, sum1, sum2, sum3):

    max_sum = 0
    for l in [(l1, sum1), (l2, sum2), (l3, sum3)]:
        if l[1] >= max_sum:
            max_sum = l[1]
            rlist = l[0]

    return rlist

n1, n2, n3 = map(int, raw_input().strip().split())

stack_list1 = deque(map(int, raw_input().strip().split()))
stack_list2 = deque(map(int, raw_input().strip().split()))
stack_list3 = deque(map(int, raw_input().strip().split()))

sum1 = sum(stack_list1)
sum2 = sum(stack_list2)
sum3 = sum(stack_list3)


while True:
    if is_all_sum_equal(sum1, sum2, sum3):
        print sum1
        break

    m_list = max_list(stack_list1, stack_list2, stack_list3, sum1, sum2, sum3)

    item = m_list.popleft()
    if m_list is stack_list1:
        sum1 -= item
    elif m_list is stack_list2:
        sum2 -= item
    else:
        sum3 -= item
