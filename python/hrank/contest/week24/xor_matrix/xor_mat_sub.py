



def deduct(items, numbers, n):
    final = []

    tmp = 0
    for i in numbers:
        tmp = tmp ^ i

    for i in xrange(n):
        res = tmp
        for item in xrange(len(items)):            
            if items[item] != 1:
                ndx = (i + item) % n
                res = res ^ numbers[ndx]
                # skipping.append(ndx)
        #print res,
        
        final.append(res)

    return final


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
# print items

final = []
#items = [1,0,1,0,1,0,1]
summ = sum(items)
r = 0

no_of_zero = sum(1 for i in xrange(n) if items[i] == 0)
no_of_one = n - no_of_zero


if summ == len(items):
    for x in numbers:
        r = r ^ x

    for i in xrange(n):
        print r,
    print
#elif no_of_zero < no_of_one:
#    ssdr = deduct(items, numbers, n)
#    for i in xrange(n):
#        print ssdr[i],
#    print
else:
    computed = {}
    last_computed = None
    to_be_computed = set()
    for i in xrange(n):
        # print last_computed    
        to_be_computed = set()
        # res = 0
    
        for item in xrange(len(items)):
            if items[item] == 1:
    
                ndx = (i + item) % n
                to_be_computed.add(ndx)
        if last_computed:
            #print "add", to_be_computed.difference(last_computed)
            #print "remove", last_computed.difference(to_be_computed)

            for item in last_computed.difference(to_be_computed):
                res = res ^ numbers[item]
            for item in to_be_computed.difference(last_computed):
                res = res ^ numbers[item]
            final.append(res)
        #if frozenset(to_be_computed) in computed:
        #    final.append(computed[to_be_computed])
        else:
            res = 0
            for iit in to_be_computed:
                res = res ^ numbers[iit]
            computed[frozenset(to_be_computed)] = res    
            final.append(res)
        last_computed = to_be_computed
        # print
    for f in final:    
        print f,
    print
