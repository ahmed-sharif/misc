# Enter your code here. Read input from STDIN. Print output to STDOUT



def optimized_bionomial_coeff(row, n):
    # items = [0 for _ in range(row + 1)]
    items = [0 for _ in xrange(n)]
    items[0] = 1
    # items[row] = 1

    # print items
    for j in xrange(1, row + 1):
        # print j
        if j & (row - j) == 0:
            res = 1
            # items[j] = 1
        else:
            res = 0
            # items[j] = 0

        index = j % n
        items[index] = items[index] ^ res
        # print items
    return items


n, m = map(int, raw_input().strip().split())

numbers = map(int, raw_input().strip().split())


items =  optimized_bionomial_coeff(m-1, n)
#print numbers
#print items

final = []

summ = sum(items)
r = 0
if summ == len(items):
    for x in numbers:
        r = r ^ x

    for i in xrange(n):
        print r,
    print        

else:

    for i in xrange(n):
        res = 0
        #print "xoring ",
        for item in xrange(len(items)):
            if items[item] == 1:

                # ndx = get_index(n, i + item)
                ndx = (i + item) % n
                # print "index=", ndx
                #print ndx,
                res = res ^ numbers[ndx]
        print res,
        final.append(res)
        #print
    print

    #print final

