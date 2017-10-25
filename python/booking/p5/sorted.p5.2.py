

from bisect import insort, bisect


passtion_position = {}

def get_length(lst):
    return max(len(x.split(",")) for x in lst)


def position_of(lst, item):
    position = bisect(lst, item)

    if position == len(lst):
        insort(lst, item)
        

    if lst[position] == item:
        return position

    return -1

    insort(lst, item)    
    return position



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


n = int(raw_input().strip())
# events = ["E"+str(i+1) for i in range(n)]

persons = []
for _ in range(n):
    inp = raw_input().strip().split()
    plist_of_person = inp[2:]
    t = set()
    for p in plist_of_person:
        position = position_of(passtion_list, p)
        t.add(position)

    persons.append(t)


events_description = []


for _ in range(n):
    inp = raw_input().strip().split()
    plist_of_events = inp[1:]
    t = set()
    for p in plist_of_events:
        position = position_of(passtion_list, p)
        t.add(position)

    events_description.append(t)

print "persons"
print persons
print "event description"
print events_description
print "passtions"
print passtion_list
# import itertools

satisfy_list = []

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

        intsct = s1.intersection(persons[p])
        if intsct:
            found = True
            #print "Event", events[e],"[",events_description[e],"]", "can satisfy person",p,persons[p]
            #
            if e==0:
                satisfy_list[e].append(str(p))
            else:
                #for indx in range(len(satisfy_list[e - 1])):
                if satisfy_list[e - 1]:
                    for item in satisfy_list[e - 1]:
                        if str(p) not in item:
                            satisfy_list[e].append(item + "," +str(p))
                        else:
                            satisfy_list[e].append(item)
                else:
                    satisfy_list[e].append(str(p))


# print satisfy_list[-1]
#for i in satisfy_list:
#    print i

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
 
