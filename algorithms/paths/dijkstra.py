from structures.priority_queue import priority_queue, low_priority, high_priority
from math import inf

def Relax(val):
    return val
SkipRelaxation = None

def default_relax(old, v, w):
    return min(old, v + w)

def dijkstra(graph, source, initial_distance=inf, source_distance=0, relax=default_relax, priority=low_priority):

    distance = [initial_distance] * graph.V
    distance[source] = source_distance
    processed = [False] * graph.V

    pq = priority_queue(graph.V, priority=priority)
    pq.extend((key, initial_distance) for key in range(1, graph.V))
    pq.change_priority(source, source_distance)

    for u, dist in pq.mutable_iter():
        processed[u] = True
        for v, w in graph.edges(u):
            if processed[v]:
                continue                
            val = relax(dist, distance[v], w)
            if val != None:
                distance[v] = val
                pq.change_priority(v, val)
    return distance