from copy import copy

from bisect import insort, bisect_left

def get_length(lst):
    return max(len(x) for x in lst)

"""
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

"""




# events = ["E"+str(i+1) for i in range(n)]

persons = []
events_description = []
satisfy_list = []

n = int(raw_input().strip())

# @profile
def take_input(n):
    for _ in range(n):
        inp = raw_input().strip().split()
        persons.append(set(inp[2:]))

    for _ in range(n):
        inp = raw_input().strip().split()
        events_description.append(set(inp[1:]))

# @profile
def generate_mat():
    this_round = [0 for _ in xrange(len(persons))]
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
            #print "check"
            intsct = s1.intersection(persons[p])
            if intsct:
                found = True
                #print "Event", events[e],"[",events_description[e],"]", "can satisfy person",p,persons[p]
                #
                print "E",e,"satisfy",p
                if e==0:
                    # satisfy_list[e].append(str(p))
                    satisfy_list[e].append([p])
                else:
                    #for indx in range(len(satisfy_list[e - 1])):
                    if satisfy_list[e - 1]:
                        print len(satisfy_list[e - 1])
                        if len(satisfy_list[e - 1]) > 1000 and len(satisfy_list[e - 1]) < 2000:
                            print satisfy_list[e - 1]
                        for item in satisfy_list[e - 1]:
                            
                            t = copy(item)
                            #t = item

                            position_of_item = bisect_left(item, p)

                            if position_of_item == len(item) or item[position_of_item] != p:
                                insort(t, p)

                                #if p not in item:
                                #print "add"
                                #    t.append(p)
                                
                                # satisfy_list[e].append(item + "," +str(p))
                                #if t not in satisfy_list[e]: 
                                #    satisfy_list[e].append(t)
                                satisfy_list[e].append(t)
                            else:
                                satisfy_list[e].append(t)
                    else:
                        satisfy_list[e].append([p])

# @profile
def print_op():
    # print satisfy_list[-1]
    for i in satisfy_list:
        print i
    #print satisfy_list
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


take_input(n)
generate_mat()
print_op()     
