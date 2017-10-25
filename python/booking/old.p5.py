

"""
n = int(raw_input().strip())

persons = []
for _ in range(n):
    inp = raw_input().strip().split()
    persons.append(inp[2:])


events = []


for _ in range(n):
    inp = raw_input().strip().split()
    events.append(inp[1:])
"""


n = 3
persons = [
    ["museum", "wine", "bike"],
    ["museum", "flower"],
    ["hike", "bike"]
]

events_description = [
    ["bike", "wine"],
    ["museum"],
    ["flower"]
]

events = [
    "E1","E2","E3"
]
"""
satisfied = {}
prev_key = None
for x in range(len(events)):
    key = ",".join(events[:x+1])
    #print key
    if not prev_key:
        prev_key = key
        for y in range(x+1):
            print events[y],

            for no, p in enumerate(persons):

                print p
                print events[y]
                intsct = set(p).intersection(set(events_description[y]))
                print intsct
                if intsct:
                    if key in satisfied:
                        satisfied[key].append(no)
                    else:
                        satisfied[key] = [no]
    else:
"""
import itertools
res = []
new_res = []
for x in range(len(events)):
    if x == 0:
        for no, p in enumerate(persons):

            #print p
            #print events[y]
            intsct = set(p).intersection(set(events_description[x]))
            #print intsct
            if intsct:
                res.append(set([no]))
                #if key in satisfied:
                #    satisfied[key].append(no)
                #else:
                #    satisfied[key] = [no]
    else:
        print "x=",x
        print "res", res
        tres = []
        new_res = []
        for no, p in enumerate(persons):
            print "event=",events_description[x]
            print "person=",p
            intsct = set(events_description[x]).intersection(set(p))
            print intsct
            if intsct:
                print "match found"
                tres.append(no)
                print tres

                #for dd in range(len(res)):
                #    res[dd].add(no)
        print "------"
        for this_res in res:
            print "this_res=", this_res
            print "tres=", tres
            ano_res = list(itertools.product(tres, this_res))
            
            ano_res = [a for a in ano_res if len(set(a))==len(a)]
            new_res.extend(ano_res)
            print "ano_res=",ano_res
        print "------"
        #res = list(itertools.product(tres, res))
        res = new_res        
        # break


print new_res
    #print res
#print res


        

                    


    
