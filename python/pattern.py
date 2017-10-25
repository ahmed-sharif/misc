G=["7283455864",
"6731158619",
"8988242643",
"3830589324",
"2229505813",
"5633845374",
"6473530293",
"7053106601",
"0834282956",
"4607924137"
]

R=10
C=10

r=3
c=4

P=["9505",
"3845",
"3530"
]

def find_all(G, P):
  for i in xrange(R - r + 1):
    for j in xrange(C - c + 1):
      found = True
      for k in xrange(r):
        
        p1 = G[i+k][j: j+c]
        if p1 != P[k]:
          found = False
          break
      if found:
        return 'YES'
  return 'NO'

print find_all(G, P)
