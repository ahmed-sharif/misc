from pprint import pprint
from collections import deque

def dfs(G, source):
    V = G['V']
    AL = G['AL']

    colors = {}
    parents = {}
    discover_time = {}
    finish_time = {}

    for vertix in V:
        colors[vertix] = 'WHITE'
    time_stamp = 1
    for vertix in V:
        if colors[vertix] == 'WHITE':
            print vertix
            time_stamp = dfs_visit(vertix, AL, colors, parents, discover_time, finish_time, time_stamp=time_stamp)

    pprint(colors)
    pprint(parents)
    print "discovery time"
    pprint(discover_time)
    print "finish time"
    pprint(finish_time)


def dfs_visit(vertix, adjacency_list, colors, parents, discover_time, finish_time, time_stamp):
    colors[vertix] = 'GRAY'
    discover_time[vertix] = time_stamp
    time_stamp += 1
    for neighbor in adjacency_list[vertix]:
        if colors[neighbor] == 'WHITE':
            parents[neighbor] = vertix
            time_stamp = dfs_visit(neighbor, adjacency_list, colors, parents, discover_time, finish_time, time_stamp)
        elif colors[neighbor] == 'GRAY':
            print "back edge", vertix, "-->", neighbor
        else:
            print "forward edge", vertix, "-->", neighbor
    colors[vertix] = 'BLACK'
    finish_time[vertix] = time_stamp
    time_stamp += 1
    return time_stamp

# example from coremen 3e pg 605
vertexes = ['u', 'v', 'w', 'x', 'y', 'z']

edges = {
    'z': ['z'],
    'u': ['v', 'x'],
    'v': ['y'],
    'w': ['y', 'z'],
    'x': ['v'],
    'y': ['x']
}

G = {'V': vertexes, 'AL': edges}


dfs(G, 's')