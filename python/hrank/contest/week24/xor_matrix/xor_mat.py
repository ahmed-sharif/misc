import copy

def p_item(item):
    for i in item:
        print i,
    print


def manually_generate(item, n):
    temp = [0 for _ in range(len(item))]
    for x in range(n):
        for i in range(len(item)-1):
            temp[i]= item[i] ^ item[i+1]

        temp[len(item)-1] = item[len(item)-1] ^ item[0]
        # print temp
        # p_item(temp)
        item = copy.copy(temp)
    return temp


def get_index(n, index):
    return index % n


def optimized_bionomial_coeff(row, n):
    # items = [0 for _ in range(row + 1)]
    items = [0 for _ in range(n)]
    items[0] = 1
    # items[row] = 1

    # print items
    for j in range(1, row + 1):
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

def generate_bionomial_coeff(row):
    items = [0 for _ in range(row + 1)]
    items[0] = 1
    items[row] = 1

    for j in range(1, row):
        if j & (row - j) == 0:
            items[j] = 1
        else:
            items[j] = 0
    return items


n, m = map(int, raw_input().strip().split())

numbers = map(int, raw_input().strip().split())

#print "input=",
#print numbers
#print "rows=", m
"""
print optimized_bionomial_coeff(m-1, n)

items = generate_bionomial_coeff(m-1)

print items


for i in range(n):
    res = 0
    for item in range(len(items)):
        if items[item] == 1:

            ndx = get_index(n, i + item)
            # print "index=", ndx
            res = res ^ numbers[ndx]
    print res,
print


p_item(manually_generate(numbers, m - 1))


"""

items =  optimized_bionomial_coeff(m-1, n)


for i in range(n):
    res = 0
    for item in range(len(items)):
        if items[item] == 1:

            ndx = get_index(n, i + item)
            # print "index=", ndx
            res = res ^ numbers[ndx]
    print res,
print
