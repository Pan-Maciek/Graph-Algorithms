def bfs(graph, source, target, condition=None):
    """
    Breadth first search with optional condition while selecting edges.
    O(|V|+|E|) when condition=None
    O(|V|+|E| * c) where c is time complexity of condition
    """
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