from collections import deque

def dfs(graph, source, target, condition=None, process=None):
    visited, stack = [False] * graph.V, deque()
    stack.append(source)

    while stack:
        u = stack.pop()
        visited[u] = True
        if u == target:
            break
        if condition != None:
            for edge in graph.edges(u):
                u, v, _ = edge
                if not visited[v] and condition(edge):
                    if process != None:
                        process(edge)
                    stack.append(v)
        else:
            for edge in graph.edges(u):
                u, v, _ = edge
                if not visited[v]:
                    if process != None:
                        process(edge)
                    stack.append(v)
    return visited