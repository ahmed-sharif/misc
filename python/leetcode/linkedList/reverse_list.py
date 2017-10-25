


class LinkedNode(object):
    def __init__(self, data):
        self.data = data
        self.nextnode = None


def print_list(head):
    temp_head = head
    while temp_head:
        
        print temp_head.data
        # print temp_head
        temp_head = temp_head.nextnode
    print

def reverse_list(original_head):
    head = original_head
    previous = None
    while head:
        print head
        temp = head.nextnode
        head.nextnode = previous
        previous = head
        head = temp
    original_head = previous
    print "ttt"
    print original_head
    print previous
    print "ttt"
    return previous
     


org = [x for x in xrange(10)]


head = LinkedNode(0)


temp_head = head

for i in xrange(len(org)):
    temp_head.data = i

    if i != len(org) - 1:
        temp_head.nextnode = LinkedNode(0)

        temp_head = temp_head.nextnode

print_list(head)
print_list(head)
print_list(head)
print "asdd", head
r=reverse_list(head)
print "head", head
print "r", r
print "reverse"
print_list(r)
