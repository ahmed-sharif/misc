# Enter your code here. Read input from STDIN. Print output to STDOUT
#from itertools import combinations 
import re
#from math import acos, sin, cos

"""

{
    "food",     
    "skating"

}

"""

s = "food and fooddd and skate skates"
tokens = ['fooddd', 'and', 'skate', 'skates']

def incl(p, tokens):
    for t in tokens:
        if t.find(p) >= 0:
            return True
    return False



from collections import defaultdict
import string
start_time = 1465945200
end_time = 1468537200

no_passions, no_reviews = raw_input().strip().split()
no_passions = int(no_passions)
no_reviews = int(no_reviews)

passions = []
for _ in range(no_passions):
    passions.append(raw_input().strip().lower())


passion_scores = defaultdict(dict)

for _ in range(no_reviews):
    r, t = raw_input().strip().split()
    t = int(t)

    porint = 0

    b = raw_input().strip()
    # passion_scores[p].append((r, porint))
    porint = 0
    if t >= start_time and t < end_time:
        porint += 20
    else:
        porint += 10
    if len(b) >= 100:
        porint += 20
    else:
        porint += 10
    
    tokens = map(string.lower, re.split(r'\W+', b))
    for p in passions:
        if p in tokens or incl(p, tokens):

            passion_scores[p][r] = passion_scores[p].get(r, 0) + porint


print passion_scores

for p in passions:
    if p in passion_scores:
        scrs = passion_scores[p]
        if len(scrs) == 1:
            print scrs.keys()[0]
        else:
            # print scrs
            temp_rids = [int(s) for s in scrs]
            print min(temp_rids)
    else:
        print -1