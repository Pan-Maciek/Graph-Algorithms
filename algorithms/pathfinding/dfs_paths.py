from graph import graph, not_visited, path as create_path

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