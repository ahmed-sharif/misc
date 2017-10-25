class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        print A
        r = len(A)
        c = len(A[0])
        
        #index_of_zeroes = []
        
        rrs = [0 for _ in xrange(r)]
        ccs = [0 for _ in xrange(c)]
        
        for i in xrange(r):
            for j in xrange(c):
                if A[i][j] == 0:
                    #print i, j
                    rrs[i] = 1
                    ccs[j] = 1
        print rrs
        print ccs
        for x, row in enumerate(rrs):
            if row == 1:
                for j in xrange(c):
                    A[x][j] = 0
        
        
        for y, col in enumerate(ccs):
            if col == 1:
                for i in xrange(r):
                    A[i][y] = 0                
        
        return A    
        """
            total_zero_in_row = c - sum(A[i])
            zero_found = 0
            if total_zero_in_row == c:
                for j in xrange(c):
                    index_of_zeroes.append((i, j))
                    
            elif total_zero_in_row > 0:
                for j in xrange(c):
                    if A[i][j] == 0:
                        index_of_zeroes.append((i, j))
                        zero_found += 1
                        
                        if zero_found >= total_zero_in_row:
                            break
        
        for item in index_of_zeroes:
            row = item[0]
            col = item[1] 
            for j in xrange(c):
                A[row][j] = 0
            
            for i in xrange(r):
                A[i][col] = 0
        return A        
        """


s = Solution()



A = [
  [0, 1],
  [0, 1]
]

print s.setZeroes(A)
