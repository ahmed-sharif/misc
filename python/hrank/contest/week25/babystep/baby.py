


q = int(raw_input().strip())
for _ in xrange(q):
    a, b, d = map(int, raw_input().strip().split())

    if d == 0:
        print 0
    # if d is less than both a and b
    elif d < a and d < b:
        print 2
    elif d > a and d < b:
        print 2
    elif d == a or d == b:
        print 1
    elif d < (a + b):
        print 2
    else:
        # print "h"
        total_left = d / b
        remaining = d % b
        if remaining:
            #aaaa = remaining / a
            #rem = remaining % a
            #if rem:
            #    aaaa += 2
            if remaining == a:
                total_left += 1
            else:
                total_left += 2

        curr = b
        rems = d - b
        # rems = 0
        tots = 1
        while rems > (a + b):
            #print "ddddd",tots, rems
            rems -= b
            tots += 1
        #print rems    
        tots += 2

        total_left = min(tots, total_left)


        curr = b
        rems = d - b
        if d / b > 1:
            tots = 1
        else:
            tots = 0
        while rems > (b + b):
            #print "ddddd",tots, rems
            rems -= b
            tots += 1
        # print rems    
        tots += 2
        total_left = min(tots, total_left)

        total_right = d / b + 1
        # print total_right
        remaining = total_right * b - d
        if remaining:
            if remaining == a:
                total_right += 1
            else:
                total_right += 2
            #aaaa = remaining / a
            #rem = remaining % a
            #if rem:
            #    aaaa += 2
            #total_right += aaaa
        # print total_left, total_right
        r = min(total_left, total_right)
        if d % a == 0:
            r = min(r, d/a)
        print r
