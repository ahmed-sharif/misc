# https://www.hackerrank.com/challenges/even-tree

def extended_dfs(G):
    """
    In addition to calculating discovery and finish time,
    it also computes number of children of each node including the node itself
    we can only remove node with even number of children
    """
    V = G['V']
    AL = G['E']

    colors = {}
    parents = {}
    discover_time = {}
    finish_time = {}
    node_count_rooted_at = {}

    for vertix in V:
        colors[vertix] = 'WHITE'
    time_stamp = 1
    for vertix in V:
        if colors[vertix] == 'WHITE':
            time_stamp = dfs_visit(vertix, AL, colors, parents, discover_time, finish_time, time_stamp, node_count_rooted_at)

    removed_edges = []
    processed_edge = []
    for vertix in V:
        for  neighbor in AL[vertix]:
            edge = (min(vertix, neighbor), max(vertix, neighbor))
            if node_count_rooted_at[neighbor] and node_count_rooted_at[neighbor] % 2 == 0:

                if edge not in removed_edges and edge not in processed_edge:                     
                    removed_edges.append(edge)
                else:
                    processed_edge.append(edge)
            else:
                processed_edge.append(edge)

    print len(removed_edges)


def dfs_visit(vertix, adjacency_list, colors, parents, discover_time, finish_time, time_stamp, node_count_rooted_at):
    colors[vertix] = 'GRAY'
    discover_time[vertix] = time_stamp
    time_stamp += 1
    for neighbor in adjacency_list[vertix]:
        if colors[neighbor] == 'WHITE':
            parents[neighbor] = vertix
            time_stamp = dfs_visit(neighbor, adjacency_list, colors, parents, discover_time, finish_time, time_stamp, node_count_rooted_at)

    colors[vertix] = 'BLACK'
    finish_time[vertix] = time_stamp
    node_count_rooted_at[vertix] = (finish_time[vertix] - discover_time[vertix] + 1) / 2
    time_stamp += 1
    return time_stamp

N, M = raw_input().strip().split()
N, M = int(N), int(M)

vertexes = [n for n in xrange(1, N + 1)]
edges = {}

for v in vertexes:
    edges[v] = []

for _ in xrange(M):
    i, j = raw_input().strip().split()
    i, j = int(i), int(j)
    edges[i].append(j)
    edges[j].append(i)

G = {'V': vertexes, 'E': edges}

extended_dfs(G)