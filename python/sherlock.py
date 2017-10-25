
"""
# case 1
aaa bbb c         --- YES
2:2  1:1
# case 2
aaa bbb ccc dddd  --- YES
3:3  4:1
# case 3
aaa bbb ccc d     --- YES
3:3 1:1
aaa bb
3:1 2:1               YES
aaa b
3:1 1:1
-----------------------------
aaaaa bb             ----NO
5:1 2:1              
aaa bbb cc           --- NO
3:2  2:1
aaa bbb cc dd
3:2 2:2  
aaa bbb c d 
3:2  1:2
aaa bbbbb ccc ddd    --- NO
3:3    5:1
aaaaa bb ccccc       --- NO
5:2   2:1
"""
from collections import defaultdict
inp_str = raw_input().strip()
char_count = defaultdict(int)
value_count = defaultdict(int)
for c in inp_str:
    char_count[c] += 1
for _, val in char_count.iteritems():
    value_count[val] += 1
kys = value_count.keys()
if len(value_count) == 1:
    print "YES"
elif len(value_count) == 2:
    # abs diff 1
    if value_count[kys[0]] == 1 or value_count[kys[1]] == 1:
        # both value 1
        if value_count[kys[0]] == 1 and value_count[kys[1]] == 1:
            if abs(kys[0] - kys[1]) == 1:
                print "YES"
            elif min([kys[0] , kys[1]]) == 1:
                print "YES"
            else:
                print "NO"
        elif value_count[min([kys[0], kys[1]])] == 1:
            if min([kys[0], kys[1]]) == 1:
                print "YES"
            else:
                print "NO"
        else:
            if abs(kys[0] - kys[1]) == 1:
                print "YES"
            else:
                print "NO"
        """        
        one_key = kys[0]
        if value_count[kys[1]] == 1:
            one_key = kys[0]

        if value_count[max([kys[0], kys[1]])] == 1:
            print "YES"
        elif min([kys[0], kys[1]])
            print "YES"        
        """
    else:
        # value is not 1
        print "NO"
else:
    print "NO"