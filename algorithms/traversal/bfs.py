from collections import deque

def bfs(graph, source, target, condition=None, process=None):
    visited, queue = [False] * graph.V, deque()
    queue.append(source)

    while queue:
        u = queue.popleft()
        if visited[u]:
            continue
        visited[u] = True
        if u == target:
            break
        if condition != None:
            for edge in graph.edges(u):
                u, v, _ = edge
                if not visited[v] and condition(edge):
                    if process != None:
                        process(edge)
                    queue.append(v)
        else:
            for edge in graph.edges(u):
                u, v, _ = edge
                if not visited[v]:
                    if process != None:
                        process(edge)
                    queue.append(v)
    return visited