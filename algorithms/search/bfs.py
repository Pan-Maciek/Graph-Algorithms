def bfs(graph, source, target, condition=None):
    visited, queue = [False] * (graph.V), [source]

    if condition == None:
        while queue:
            u = queue.pop(0)
            if visited[u]:
                continue
            visited[u] = True
            if u == target:
                break
            queue.extend(v for v in graph.neighors(u) if not visited[v])
    else:
        while queue:
            u = queue.pop(0)
            if visited[u]:
                continue
            visited[u] = True
            if u == target:
                break
            queue.extend(v for v, w in graph.edges(u) if not visited[v] and condition((u, v, w)))
            
    return visited[target]