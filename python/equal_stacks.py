n1, n2 , n3 = map(int,raw_input().strip().split(' '))

n1_list = map(int,raw_input().strip().split(' '))
n2_list = map(int,raw_input().strip().split(' '))
n3_list = map(int,raw_input().strip().split(' '))

n1_list.reverse()
n2_list.reverse()
n3_list.reverse()

sum_n1 = sum(n1_list)
sum_n2 = sum(n2_list)
sum_n3 = sum(n3_list)




#print n1, n2, n3

#print n1_list
#print n2_list
#print n3_list

# print sum_n1, sum_n2, sum_n3

if sum_n1 == sum_n2 and sum_n2 == sum_n3:
    print sum_n1
else:
    while True:
        
        if max((sum_n1, sum_n2, sum_n3)) == sum_n1:
            # print "max n1"
            while sum_n1 > min((sum_n2, sum_n3)):
                sum_n1 = sum_n1 - n1_list.pop()
            if sum_n1 == sum_n2 and sum_n2 == sum_n3:
                print sum_n1
                break

        elif max((sum_n1, sum_n2, sum_n3)) == sum_n2:
            # print "max n2"
            while sum_n2 > min((sum_n1, sum_n3)):
                sum_n2 = sum_n2 - n2_list.pop()
            if sum_n1 == sum_n2 and sum_n2 == sum_n3:
                print sum_n1
                break
        else:        
        # if max((sum_n1, sum_n2, sum_n3)) == sum_n3:
            # print "max n3"
            while sum_n3 > min((sum_n1, sum_n2)):
                sum_n3 = sum_n3 - n3_list.pop()
            if sum_n1 == sum_n2 and sum_n2 == sum_n3:
                print sum_n1
                break
        