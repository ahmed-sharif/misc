class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
        if B > A:
            A, B = B, A
        
        r = A % B
        print r
        while r != 0:
            # temp = B
            A = B
            B = r
            print A, B
            r = A % B
        return B

s = Solution()

print s.gcd(6, 4)
