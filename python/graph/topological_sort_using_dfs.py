# example from coremen 3e pg 613

from pprint import pprint
from collections import deque

def dfs(G, source):
    V = G['V']
    AL = G['AL']

    colors = {}
    parents = {}
    discover_time = {}
    finish_time = {}

    topological_order = deque()

    for vertix in V:
        colors[vertix] = 'WHITE'
    time_stamp = 1
    for vertix in V:
        if colors[vertix] == 'WHITE':
            
            time_stamp = dfs_visit(vertix, AL, colors, parents, discover_time, finish_time, time_stamp, topological_order)

    # pprint(colors)
    print "parents"
    pprint(parents)
    print "discovery time"
    pprint(discover_time)
    print "finish time"
    pprint(finish_time)
    print "order", topological_order


def dfs_visit(vertix, adjacency_list, colors, parents, discover_time, finish_time, time_stamp, topological_order):
    colors[vertix] = 'GRAY'
    discover_time[vertix] = time_stamp
    time_stamp += 1
    for neighbor in adjacency_list[vertix]:
        if colors[neighbor] == 'WHITE':
            parents[neighbor] = vertix
            time_stamp = dfs_visit(neighbor, adjacency_list, colors, parents, discover_time, finish_time, time_stamp, topological_order)
        elif colors[neighbor] == 'GRAY':
            pass
            # print "back edge", vertix, "-->", neighbor
        else:
            pass
            # print "forward edge", vertix, "-->", neighbor
    colors[vertix] = 'BLACK'
    finish_time[vertix] = time_stamp
    topological_order.appendleft(vertix)
    time_stamp += 1
    return time_stamp


vertexes = ['shirt', 'watch', 'undershorts', 'socks', 'pant', 'shoes', 'belt', 'tie', 'jacket']

edges = {
    'undershorts': ['pant', 'shoes'],
    'socks': ['shoes'],
    'pant': ['belt'],
    'shoes': [],
    'watch': [],
    'shirt': ['tie', 'belt'],
    'belt': ['jacket'],
    'tie': ['jacket'],
    'jacket': []
}

G = {'V': vertexes, 'AL': edges}


dfs(G, 's')