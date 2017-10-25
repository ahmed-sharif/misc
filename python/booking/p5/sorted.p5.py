
import sys
from bisect import insort, bisect_left

def get_length(lst):
    return max(len(x.split(",")) for x in lst)


n = 4
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

events = ["E1", "E2", "E3", "E4"]


passtion_list = []
passtion_index = {}

def insert_all(lst):
    # print lst
    for item in lst:
        position = bisect_left(passtion_list, item)
        # print "posision of", item, "=",str(position)
        # print passtion_list, position, lst

        if position == len(passtion_list):
            insort(passtion_list, item)
        else:
            if passtion_list[position] != item:
                insort(passtion_list, item)

n = int(raw_input().strip())
# events = ["E"+str(i+1) for i in range(n)]

persons = []
for _ in range(n):
    inp = raw_input().strip().split()
    # persons.append(set(inp[2:]))
    temp = inp[2:]
    persons.append(temp)
    insert_all(temp)


events_description = []


for _ in range(n):
    inp = raw_input().strip().split()
    temp = inp[1:]
    # events_description.append(set(inp[1:]))
    events_description.append(temp)
    insert_all(temp)

#print "ev"
##print events_description
#print "person"
#print persons
#print "passtion list"
#print passtion_list


for i, p in enumerate(passtion_list):
    passtion_index[p] = i


for i in xrange(len(persons)):
    t = set()
    plist = persons[i]
    for p in plist:
        t.add(passtion_index[p])
    persons[i] = t


for i in xrange(len(events_description)):
    t = set()
    plist = events_description[i]
    for p in plist:
        t.add(passtion_index[p])
    events_description[i] = t
#print "ev"
#print events_description
#print "person"
#print persons
#print "passtion list"
#print passtion_list
#print "passtion index"
#print passtion_index


def has_intersection(lst1, lst2):
    for i in lst1:
        pass


#
#sys.exit(0)
# import itertools

satisfy_list = []
#print events_description[5]
#print persons[1]
#print persons[0]
#import sys
#sys.exit(0)


for e in xrange(len(events_description)):
    satisfy_list.append([])
    found = False
    if e  > 1:
        if not satisfy_list[e -1] and satisfy_list[e-2]:
            satisfy_list[e -1] = satisfy_list[e-2]
    # s1 = set(events_description[e])        
    s1 = events_description[e]
    for p in xrange(len(persons)):
        
        # s2 = set(persons[p])
        #print "checking"
        intsct = s1.intersection(persons[p])
        if intsct:
            found = True
            #print "Event", events_description[e],"[",events_description[e],"]", "can satisfy person",p,persons[p]
            print "event", e, "can satisfy",p 
            if e==0:
                satisfy_list[e].append([str(p)])
            else:
                #for indx in range(len(satisfy_list[e - 1])):
                if satisfy_list[e - 1]:
                    for item in satisfy_list[e - 1]:
                        print item
                        if str(p) not in item:
                            # satisfy_list[e].append(item + "," +str(p))
                            item.append(str(p))
                            satisfy_list[e].append(item)
                            #satisfy_list[e].append(str(p))
                        else:
                            satisfy_list[e].append(item)
                else:
                    satisfy_list[e].append(str(p))
    print "after event", str(e), satisfy_list[e]


# print satisfy_list[-1]
#for i in satisfy_list:
#    print i


sys.exit(0)
if not satisfy_list[-1]:
    if n == 1:
        print 0
    else:
        if n == 2:
            if satisfy_list[-2]:
                # res = max(len(x) for x in satisfy_list[-2])
                print get_length(satisfy_list[-2])
                
            else:
                print 0

        else:
            # satisfy_list[-1] = satisfy_list[-2]
            for start in range(n -1, -1, -1):
                if satisfy_list[start]:
                    print get_length(satisfy_list[start])
                    break
            else:
                print 0

else:
    print get_length(satisfy_list[-1])
 
