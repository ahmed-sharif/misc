# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp_l1 = l1
        temp_l2 = l2
        
        result = ListNode(0)
        temp_r = result
        carry = 0
        
        while True:
            first = 0
            second = 0
            
            if temp_l1:
                first = temp_l1.val
                temp_l1 = temp_l1.next
            
            if temp_l2:
                second = temp_l2.val
                temp_l2 = temp_l2.next

            if temp_l1 is None and temp_l2 is None:
                if carry:
                    temp_r.val = carry
                else:
                    temp_r = None
                break
                    
            
            r = first + second + carry
            
            carry = r / 10
            
            new_digit = r % 10
            
            temp_r.val = new_digit
            temp_r.next = ListNode(0)
            temp_r = temp_r.next
        return result
            

l1 = ListNode(2)
l2 = ListNode(4)
l3 = ListNode(3)

l1.next = l2
l2.next = l3


m1 = ListNode(5)
m2 = ListNode(6)
m3 = ListNode(4)            
                
m1.next = m2
m2.next = m3


s = Solution()
r = s.addTwoNumbers(l1, l2)

while True:
    if r is None:
        break
    print r.val
    r = r.next

            
            
        
