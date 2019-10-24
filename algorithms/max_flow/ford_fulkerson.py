from structures.graph import residual_graph, min_weight
from algorithms.paths.dfs import dfs_path
from structures.path import min_along_path
from math import inf

positive_weight = min_weight(0, strong=True)
def max_flow(graph, source, sink, find_path=dfs_path):
    rg = graph if isinstance(graph, residual_graph) else residual_graph(graph)
    flow = 0

    while True:
        path = find_path(rg, source, sink, condition=positive_weight, path_accumulator=min_along_path, initial_acc_state=inf)
        if path == None:
            break
        for u, v in path:
            rg.dec_weight(u, v, path.accumulated)
            rg.inc_weight(v, u, path.accumulated)
        flow += path.accumulated

    return flow