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
            stack.extend(edge[0] for edge in graph.edges(u) if not visited[edge[0]] and condition(edge))

    return visited[target]
