print 100

passion = ['a' for _ in range(97)]
passion = ''.join(passion)
print passion

passions = [ passion + str(x) for x in range(1,1001)]


for i in range(100):
    p_strs =[passions[p] for p in range(i,i+100)]
    
    output = "{0} 100 ".format(i+1)