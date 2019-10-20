def bfs(graph, source, target, condition=None, process=None):
    visited, queue = [False] * graph.V, [source]

    while queue:
        u = queue.pop(0)
        if visited[u]:
            continue
        visited[u] = True
        if u == target:
            break
        if condition != None:
            for v, w in graph.edges(u):
                edge = (u, v, w)
                if not visited[v] and condition(edge):
                    if process != None:
                        process(edge)
                    queue.append(v)
        else:
            for v, w in graph.edges(u):
                if not visited[v]:
                    if process != None:
                        process((u, v, w))
                    queue.append(v)
    return visited