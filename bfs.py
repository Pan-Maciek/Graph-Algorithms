from graph import graph
def bfs(G: graph, s):
    visited, queue = set(), [s]
    while queue:
        v = queue.pop(0)
        if v not in visited:
            visited.add(v)
            queue.extend(u for u in G.neighbors_of(v) if u not in visited)
            yield v