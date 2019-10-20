from algorithms.traversal.bfs import bfs as bfs_traversal

def bfs(graph, source, target, condition=None):
    return bfs_traversal(graph, source, target, condition=condition)[target]