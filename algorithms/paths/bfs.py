from structures.path import path
from algorithms.traversal.bfs import bfs as bfs_traversal

def bfs_path(graph, source, target, condition=None):
    previous = [None] * graph.V
    def process_edge(edge):
        u, v, _ = edge
        previous[v] = u

    bfs_traversal(graph, source, target, condition=condition, process=process_edge)
    return path.from_previous_list(previous, target)
