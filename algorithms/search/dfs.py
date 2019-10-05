from graph import graph, not_visited

def dfs(G: graph, s):
    visited, stack = set(), [s]
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.add(v)
            stack.extend(not_visited(visited, G.neighbors_of(v)))
            yield v
