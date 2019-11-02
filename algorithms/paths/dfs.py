from structures.path import path
from algorithms.traversal.dfs import dfs as dfs_traversal

def dfs_path(graph, source, target, condition=None, path_accumulator=None, initial_acc_state=0):
    previous = [None] * graph.V
    def process_edge(edge):
        _, v, _ = edge
        previous[v] = edge

    dfs_traversal(graph, source, target, condition=condition, process=process_edge)
    return path.from_previous_list(previous, target, accumulator=path_accumulator, initial_acc_state=initial_acc_state)