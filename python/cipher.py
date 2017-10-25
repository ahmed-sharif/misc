"""
n = 7
l = 4

s = "1110100110"

start = True
f = []
res = int(s[-1])
previous = res
f.append(res)

for i in range(len(s)-2, len(s) -1 -7, -1):
    
    # print "XORING", s[i], "and", previous  
    res = int(s[i]) ^ previous
    stor = res ^ previous 
    print "i=",i,"XORING", s[i], "and", previous, "res=",res, "storing", stor


    f.append(res)
    #previous = int(s[i])
    #previous = res
    if i > len(s) -1 - 4
        previous = stor
    else:
        

f.reverse()
print f


reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) 
"""
import sys

inp = "1110111111110001"
l = 11

# def shift2(inp, l):


def conv_(inp, l):
    total = 0
    number = int(inp, 2)
    for _ in range(l):
        total ^= number
        number *= 2
    return bin(total)[2:]
"""
print "1001010"
print conv_("1001010", 4)

inp = "101111"
print inp
print conv_(inp, 2)
print "1110001"
print "-----"
inp = "10011"
print inp
print conv_(inp, 12)
print "1110111111110001"
print "---"
print inp
print conv_(inp, 3)
"""

def shift1(inp, l):
    if l==1:
        return inp

    previous = int(inp[-1])
    f = [inp[-1]]
    start = 0
    c_start = 0
    for i in range(len(inp)-2, l - 2, -1):
        res = int(inp[i]) ^ previous
        f.append(str(res))

        if start < l - 2:
            previous = int(inp[i])
        else:
            
            previous = int(inp[i]) ^ int(f[c_start])
            c_start += 1

        
        start += 1
    f.reverse()
    return ''.join(f)


inp = "1110100110"

l = 4
print shift1(inp, l)

inp = "1110001"
l = 2
print shift1(inp, l)




#sys.exit(0)
org_inp = [
    "1001010"
]

# print conv_("1001010", 4)


for inp in org_inp:
    for i in range(1, 25):
        print inp, i
        
        r = conv_(inp, i)
        print r
        rr = shift1(r, i)
        print rr
        assert shift1(conv_(inp, i), i) == inp
