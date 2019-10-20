def dfs(graph, source, target, condition=None, process=None):
    visited, stack = [False] * graph.V, [source]

    while stack:
        u = stack.pop()
        visited[u] = True
        if u == target:
            break
        if condition != None:
            for v, w in graph.edges(u):
                edge = (u, v, w)
                if not visited[v] and condition(edge):
                    if process != None:
                        process(edge)
                    stack.append(v)
        else:
            for v, w in graph.edges(u):
                if not visited[v]:
                    if process != None:
                        process((u, v, w))
                    stack.append(v)
    return visited