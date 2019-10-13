def dfs(graph, source, target, condition=None):
    visited, stack = [False] * (graph.V), [source]

    if condition == None:
        while stack:
            u = stack.pop()
            visited[u] = True
            if u == target:
                break
            stack.extend(v for v in graph.neighbors(u) if not visited[u])
    else:
        while stack:
            u = stack.pop()
            visited[u] = True
            if u == target:
                break
            stack.extend(v[0] for v in filter(condition, graph.edges(u)) if not visited[v[0]])

    return visited[target]
