from algorithms.traversal.dfs import dfs as dfs_traversal

def dfs(graph, source, target, condition=None):
    return dfs_traversal(graph, source, target, condition=condition)[target]