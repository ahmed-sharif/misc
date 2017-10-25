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
    
    visited = []

    for vertix in V:
        print "out --", vertix
        if colors[vertix] == 'WHITE':
            visited.append(vertix)
            
            while visited:
                vertix_to_process = visited.pop()
                print "poped", vertix_to_process
                colors[vertix_to_process] = 'GRAY'
                for neighbor in AL[vertix_to_process]:
                    if colors[neighbor] == 'WHITE':
                        parents[neighbor] = vertix_to_process
                        visited.append(neighbor)
                    elif colors[neighbor] == 'GRAY':
                        print "back edge", vertix, "-->", neighbor
                    else:
                        print "forward edge", vertix, "-->", neighbor
                colors[vertix_to_process] = 'BLACK'


    pprint(colors)
    pprint(parents)
    pprint(discover_time)
    pprint(finish_time)


def dfs_visit(vertix, adjacency_list, colors, parents, discover_time, finish_time, time_stamp):
    colors[vertix] = 'GRAY'
    for neighbor in adjacency_list[vertix]:
        if colors[neighbor] == 'WHITE':
            parents[neighbor] = vertix
            dfs_visit(neighbor, adjacency_list, colors, parents, discover_time, finish_time, time_stamp + 1)
    colors[vertix] = 'BLACK'




# example from coremen 3e pg 605
vertexes = ['u', 'v', 'w', 'x', 'y', 'z']

edges = {
    'z': ['z'],
    'u': ['x', 'v'],
    'v': ['y'],
    'w': ['y', 'z'],
    'x': ['v'],
    'y': ['x']
}

G = {'V': vertexes, 'AL': edges}


dfs(G, 's')