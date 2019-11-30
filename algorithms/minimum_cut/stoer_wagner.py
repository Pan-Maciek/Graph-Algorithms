from structures.priority_queue import high_priority
from algorithms.paths.dijkstra import dijkstra
from math import inf

def relax(_, v, w):
    return v + w

def find_most_tightly_connected_vertex(G, source):
    last = (0, 0, 0) # (s, t, _)

    def store_last(edge, _):
        nonlocal last
        last = edge
    
    dist = dijkstra(G, source, initial_distance=0, source_distance=1, relax=relax, priority=high_priority, process=store_last)
    s, t, _ = last
    return (s, t, dist[t])

def min_cut(G): # (warning) mutable
    m = inf
    while G.MV > 2:
        s, t, w = find_most_tightly_connected_vertex(G, 2)
        m = min(m, w)
        G.merge(s, t)
    return m