from graph import graph
from algorithms.util import not_visited

def bfs(G: graph, s):
    visited, queue = set(), [s]
    while queue:
        v = queue.pop(0)
        if v not in visited:
            visited.add(v)
            queue.extend(not_visited(visited, G.neighbors_of(v)))
            yield v