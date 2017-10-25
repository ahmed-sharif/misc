def tracefunc(frame, event, arg, indent=[0]):
      if event == "call":
          indent[0] += 2
          print "-" * indent[0] + "> call function", frame.f_code.co_name
      elif event == "return":
          print "<" + "-" * indent[0], "exit function", frame.f_code.co_name
          indent[0] -= 2
      return tracefunc

import sys
sys.settrace(tracefunc)



class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.decode_way(s)
    def check(self, c1, c2):
        if int(c1 + c2) <= 26:
            return True

        return False        

    def decode_way(self, txt):

        if len(txt) <= 1:
            return len(txt)

        result = [0 for _ in xrange(len(txt))]

        result[-1] = 1
        result[-2] = 1

        if self.check(txt[-2], txt[-1]):
            result[-2] = 2

        # start from the 3rd character from last
        start = len(txt) - 1 - 2
        while start >= 0:
            result[start] = result[start + 1]

            if self.check(txt[start], txt[start + 1]):
                result[start] += result[start + 2]

            start -= 1
        return result[0]
            


    

def main():
    item = "123412341231242342341212341234123124234234121234123412312423423412"
    #item = "1234123412312423423412123"
    #item = "12111"

    #print len(item)
    #n = decode_way(item)
    #print len(n)
    #print n
    print Solution().numDecodings(item)

main()
