n = 3
persons = [
    ["museum", "wine", "bike"],
    ["museum", "flower"],
    ["hike", "bike"],
    ["museum", "dance"]
]

events_description = [
    ["bike", "wine"],
    ["museum"],
    ["flower"],
    ["dance"]
]

events = [
    "E1","E2","E3","E4"
]

import itertools

def flat_list(l1, l2):
    lst1 = [0, 2]
    lst2 = [0, 1, 3]
    res = list(itertools.product(lst1,lst2))
    res = [r for r in res if len(set(r))==len(r)]



def flatten_list(l):
    print l
    res = []
    for item in l:
        t = list(item[1])
        t.append(item[0])
        res.append(t)
    return res



satisfy_list = []

for e in range(len(events)):
    satisfy_list.append([])
    for p in range(len(persons)):
        s1 = set(events_description[e])
        s2 = set(persons[p])

        intsct = s1.intersection(s2)
        if intsct:
            print "Event", events[e],"[",events_description[e],"]", "can satisfy person",p,persons[p]
            satisfy_list[e].append(p)

print satisfy_list
nlist = []
previous_list = [satisfy_list[0]]
#previous_list = satisfy_list[0]

for i in range(1, len(satisfy_list)):
    if not satisfy_list[i]:
        continue
    print "----"
    print previous_list
    print "----"
    nlist = []
    #for x in previous_list:
    #print "x=", x
    print "mul=",satisfy_list[i]
    res =  list(itertools.product(satisfy_list[i], previous_list))
    print "res=",res
    res = [r for r in res if len(set(r))==len(r)]
    #res = [list(r) for r in res]
    print "res=",res
    #nlist.extend(res) 
    #print nlist    
    if i > 1:
        previous_list = flatten_list(res)
    else:
        previous_list = res

print previous_list
xxd = [len(set(x)) for x in previous_list]

print xxd
print max(xxd)
