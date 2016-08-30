from itertools import izip


def is_isomorphic(w1, w2):
    forward_mappings = {}
    backward_mappings = {}

    for (l1, l2) in izip(w1, w2):

        if l1 in forward_mappings and forward_mappings[l1] != l2:
            return False

        if l2 in backward_mappings and backward_mappings[l2] != l1:
            return False

        forward_mappings[l1] = l2
        backward_mappings[l2] = l1
    return True


# "foo", "app"; returns true
print "is_isomorphic('foo','app') "
print is_isomorphic('foo','app') 
# "foo", "boa"; returns false
print "is_isomorphic('foo','boa')"
print is_isomorphic('foo','boa') 

# "bar", "foo"; returns false
print "is_isomorphic('bar','foo') "
print is_isomorphic('bar','foo') 

# "turtle", "tletur"; returns true
print "is_isomorphic('turtle','tletur')"
print is_isomorphic('turtle','tletur') 

# "ab", "ca"; returns true
print "is_isomorphic('ab','ca') "
print is_isomorphic('ab','ca') 
