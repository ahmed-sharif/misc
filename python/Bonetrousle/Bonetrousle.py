

from itertools import combinations

n = int(raw_input().strip())

for _ in range(n):
    total, item_count, trips = map(int, raw_input().strip().split())


    items = [x for x in range(1, item_count + 1)]

    for com in combinations(items, trips):
        if sum(com) == total:
            # print " ".join(com)
            for i in com:
                print i,
            print
            break
    else:
        print -1






1   2   3   4   5   6   7   8


  1   2   3   4   5

 (1,  2,  3,  0,  0),    
 (1,  2,  0,  4,  0),    
 (1,  2,  0,  0,  5),    
 (1,  0,  3,  4,  0),    
 (1,  0,  3,  0,  5),    
 (1,  0,  0,  4,  5),    
 (0,  2,  3,  4,  0),    
 (0,  2,  3,  0,  5),    
 (0,  2,  0,  4,  5),    
 (0,  0,  3,  4,  5)]    



 (0, 0, 1, 1, 1)
 (0, 1, 0, 1, 1),
 (0, 1, 1, 0, 1),
 (0, 1, 1, 1, 0),
 (1, 0, 0, 1, 1),
 (1, 0, 1, 0, 1),
 (1, 0, 1, 1, 0),
 (1, 1, 0, 0, 1)
 (1, 1, 0, 1, 0),
 (1, 1, 1, 0, 0),
 
 7
 11
 13
 14
 19
 21
 26
 28




 nCr



 n!
 /
 (n-r)!r!


 5!
 /
 3!2!



5!
/
4!1!







