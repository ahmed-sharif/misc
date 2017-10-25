def compare(a, b):
    print a, b
    print str(a) + str(b), str(b) + str(a)
    r = str(a) + str(b) < str(b) + str(a)
    print r
    if r:
        return 1
    else:
        return -1

class Solution:
    # @param A : tuple of integers
    # @return a strings
    
    def largestNumber(self, B):
        
        A = list(B)
        print A
        A.sort(cmp=compare)
        return A
        mx_len = 0
        for i in A:
            if len(str(i)) > mx_len:
                mx_len = len(str(i))
        
        # 1   2   3   4
        mx_num = '0' * mx_len
        # mx_
        for i in xrange(len(A) - 1):
            mx_num = str(A[i]) + '0' * (mx_len - len(str(A[i])))
            mx_index = i
            for j in xrange(i + 1, len(A)):
                valj = str(A[j]) + '0' * (mx_len - len(str(A[j])))
                
                if valj > mx_num:
                    mx_num = valj
                    mx_index = j
                elif valj == mx_num:
                    if A[j] < int(mx_num):
                        mx_num = valj
                        mx_index = j
            if i != mx_index:
                A[i], A[mx_index] = A[mx_index], A[i]
        
        res = ''
        for i in A:
            res = res + str(i)
        return res
                    
                    
                
s = Solution()

print s.largestNumber([3, 30, 34, 5, 9])
