import copy

def p_item(item, row):
    print "r=%3d " % row,
    for i in item:
        print "%4d" % i,
    print


def manually_generate(original_item, n):
    item = copy.copy(original_item)
    temp = [0 for _ in range(len(item))]
    for x in range(n):
        for i in range(len(item)-1):
            temp[i]= item[i] ^ item[i+1]

        temp[len(item)-1] = item[len(item)-1] ^ item[0]
        
        item = copy.copy(temp)
    return temp


def get_index(n, index):
    return index % n


for i in range(5, 25):
    print "------------------------------"
    numbers = [x for x in range(1,i+1)]
    p_item(numbers,1)
    for x in range(1, 25):
        p_item(manually_generate(numbers, x),x+1)
        
