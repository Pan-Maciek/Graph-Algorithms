from graph import graph, path as create_path
from algorithms.util import not_visited

def dfs(G: graph, s):
    visited, stack = set(), [s]
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.add(v)
            stack.extend(not_visited(visited, G.neighbors_of(v)))
            yield v

def dfs_paths(G: graph, s, t):
    visited, path = set(), []
    def paths(v):
        if v not in visited:
            visited.add(v)
            path.append(v)
            if v == t:
                yield create_path(path)
            else:
                for u in G.neighbors_of(v):
                    yield from paths(u)
            path.pop()
            visited.remove(v)
    yield from paths(s)
