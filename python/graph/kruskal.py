# example from coremen 3e pg 632

#def find_set(v_set_dict, u):
#    return v_set_dict[]
from pprint import pprint
def make_set(vertexes):
    v_set_dict = {}
    for v in vertexes:
        v_set_dict[v] = set([v])
    return v_set_dict

vertexes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

edges = {
    ('a', 'b'): 4,
    ('a', 'h'): 8,
    ('b', 'h'): 11,
    ('b', 'c'): 8,
    ('c', 'd'): 7,
    ('c', 'i'): 2,
    ('c', 'f'): 4,
    ('d', 'e'): 9,
    ('d', 'f'): 14,
    ('e', 'f'): 10,
    ('f', 'g'): 2,
    ('g', 'h'): 1,
    ('g', 'i'): 6,
    ('h', 'i'): 7
}

def make_union(v_set_dict, u, v):
    set_a = v_set_dict[u]
    set_b = v_set_dict[v]
    set_c = set_a.union(set_b)

    #if(len(v_set_dict[u]))

    v_set_dict[u] = set_c
    v_set_dict[v] = set_c

    #for item in set_c:
    #    v_set_dict[item] = set_c
    

sorted_edges = edges.keys()

v_set_dict = make_set(vertexes)


result = []

sorted_edges.sort(key=lambda x: edges[x])
#for e in sorted_edges:
#    print e, edges[e]

i = 0
for e in sorted_edges:
    print "taking", e
    if v_set_dict[e[0]] != v_set_dict[e[1]]:
        result.append(e)
        make_union(v_set_dict, e[0], e[1])
        pprint(v_set_dict)
        i += 1
        if i > 7:
            break
        
#pprint(v_set_dict)

