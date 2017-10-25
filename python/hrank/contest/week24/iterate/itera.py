
import copy
def iterate(arr):
    rep = 0
    print arr
    A = copy.copy(arr)
    while A:
        print len(A)
        B = []
        for x in A:
            for y in A:
                #print "comparing", x,y
                if x != y: 
                    B.append(abs(x-y))

        print B
        A = B
        rep = rep + 1

    return rep



print iterate([1,11])
# print iterate([12,9,13])
# print iterate([21,3,54])
print iterate([1])

"""
una Kim Claims Silver With A Superb Performance | Sochi 2014 Winter Olympics
"""