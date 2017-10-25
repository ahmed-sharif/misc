#!/bin/python



n = int(raw_input().strip())
a = map(int,raw_input().strip().split())


#a = [1 , 2 , 3, 4, 42]
#sort(a)

no_of_cut = 0

#n=4
if n == 1:
    print 2
elif n == 2:
    if a[0] == a[1]:
        print 2
    else:
        print 1
else:
    a.sort()
    temp = [a[0]]
    for i in range(1, len(a)):
        temp.append(temp[i - 1] + a[i])
        if i < 2:
            continue
        if a[i] >= temp[i-1]:
            #print "cut is needed for",a[i]
            no_of_cut += 1
    #print a    
    #print temp
    print no_of_cut











