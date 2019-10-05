from graph import graph
def dfs(G: graph, s):
    visited, stack = set(), [s]
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.add(v)
            stack.extend(u for u in G.neighbors_of(v) if u not in visited)
            yield v