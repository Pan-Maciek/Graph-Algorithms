from test_utils import test, load_directed_graph

from structures.graph import residual_graph, min_weight
from algorithms.paths.dfs import dfs_path
from structures.path import min_along_path
from math import inf

# Finding max flow in network using Ford-Fulkerson's method + dfs

@test(data='./data/lab2/flow', loader=load_directed_graph, times=1)
def run(G):
    rg, max_flow = residual_graph(G), 0
    s, t = 1, G.V - 1
    
    while True:
        path = dfs_path(rg, s, t, condition=min_weight(0, strong=True), path_accumulator=min_along_path, initial_acc_state=inf)
        if path == None:
            break
        for u, v in path:
            rg.dec_weight(u, v, path.accumulated)
            rg.inc_weight(v, u, path.accumulated)
        max_flow += path.accumulated
    return max_flow
