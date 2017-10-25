
"""

2   2   2   3   3   3   4

19

19 / 3 = 6


19 % 3 = 1

3.2 = 6 




6 + 1 = 7



19 - 7 = 12

(6 - 2) *  3 


total_3 = total / 3 = 6
reminder = total % 3 = 1

rem_r = i * 3 + reminder = 2 * 3 + 1 = 7

temp = total - rem_r = 19 - 7 = 12

(total_3 - i ) * 3 == temp

"""

2   2   2   3   3   3   4
total = 19
total_3 = total / 3 = 6
reminder = total % 3 = 1

rem_r = i * 3 + reminder = 4 * 3 + 1 = 13

temp = total - rem_r = 19 - 13 = 6

(total_3 - i ) * 3 == temp


def calc(arr):
    total = sum(arr)
    total_3 = total / 3
    reminder = total % 3
    for i in arr:
        rem_r = i * 3 + reminder
        temp = total - rem_r

        if (total_3 - i ) * 3 == temp:
            pass
        else:
            print "res", i


calc([2, 2, 2, 3, 3, 3, 4])
# calc([1,   1,   1,   2,   2,   2,   4]) 
#find_single([1,   1,   1,   2,   2,   2,   7])
#find_single([1,   1,   1,   3,   3,   3,   6])
#find_single([1,   1,   1,   3,   3,   3,   36])

#find_single([1,   1,   1,   3,   3,   3,   2]) 




def find_single(arr):
    print arr
    total = sum(arr)

    total_three = total / 3
    reminder = total % 3

    print "total", total, "total_3", total_three, "reminder", reminder
    # total_three += 1
    # print total_three

    for i in arr:
        # lets assume i is present 3 times
        print "\t", "i", i
        temp = 3 * i

        print "temp", temp

        temp_three = temp / 3


        print "temp_three", temp_three

        print "total - temp", total - temp

        print "(total_three - ", i , ") * 3", (total_three - i) * 3


        if ((total_three - i) * 3)  != (total - reminder - 3 * temp_three) or temp >= total:
            print "new=", i

        if (total - temp) < (total_three - i) * 3:
            print "result", i

        #if (total_three - temp_three) != (total - temp) / 3:
        #    print i
        #    return i



"""
#13

#4

#temp = 12

#4

13

3 * 4


13 - 3

10

3


4


1

3
"""

#find_single([1,   1,   1,   2,   2,   2,   4]) 
#find_single([1,   1,   1,   2,   2,   2,   7])
#find_single([1,   1,   1,   3,   3,   3,   6])
#find_single([1,   1,   1,   3,   3,   3,   36])

#find_single([1,   1,   1,   3,   3,   3,   2]) 

"""
total 14
14 / 3 = 4
i=2

i * 3 = 6



14 - 6 = 8
"""



"""
total 13
13 / 3 = 4
4 * 3 = 12
3_left = 4 - 3 = 1
13 - 12  < 1 * 3
"""



