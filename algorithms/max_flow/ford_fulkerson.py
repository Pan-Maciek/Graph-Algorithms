from structures.graph import residual_graph, flow_edge
from algorithms.paths.dfs import dfs_path
from structures.path import min_bandwidth
from math import inf

def max_flow(graph, source, sink, find_path=dfs_path):
    rg = graph if isinstance(graph, residual_graph) else residual_graph(graph)
    flow = 0

    while True:
        path = find_path(rg, source, sink, condition=flow_edge.not_saturated, path_accumulator=min_bandwidth, initial_acc_state=inf)
        if path == None:
            break
        for u, v in path:
            rg.edge(u, v).flow += path.accumulated
            rg.edge(v, u, flow_edge(0)).flow -= path.accumulated
        flow += path.accumulated

    return flow