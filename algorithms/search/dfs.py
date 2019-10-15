def dfs(graph, source, target, condition=None):
    visited, stack = [False] * (graph.V), [source]

    if condition == None:
        while stack:
            u = stack.pop()
            visited[u] = True
            if u == target:
                break
            stack.extend(v for v in graph.neighbors(u) if not visited[v])
    else:
        while stack:
            u = stack.pop()
            visited[u] = True
            if u == target:
                break
            stack.extend(v for v, w in graph.edges(u) if not visited[v] and condition((u, v, w)))

    return visited[target]
