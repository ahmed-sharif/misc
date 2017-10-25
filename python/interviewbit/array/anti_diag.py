class Solution:
    # @param a : list of list of integers
    # @return a list of list of integers
    def diagonal(self, a):
        n = len(a)
        res = []
        for i in xrange(n):
            temp = []
            x = 0
            y = i
            for j in xrange(i + 1):
                temp.append(a[x][y])
                x += 1
                y -= 1
            res.append(temp)
        
        for i in xrange(n - 1, 0, -1):
            temp = []
            x = n - i
            y = n - 1
            print
            for j in xrange(i):
                print x,y
                temp.append(a[x][y])
                x += 1
                y -= 1
            res.append(temp)
        return res
                
                
                
                
                

s = Solution()

a= [ [1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]
]


print s.diagonal(a)
