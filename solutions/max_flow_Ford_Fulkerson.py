from test_utils import test, load_directed_flow_graph

from algorithms.max_flow.ford_fulkerson import max_flow
from structures.graph import residual_graph

# Finding max flow in network using Ford-Fulkerson's method + dfs

@test(data='./data/lab2/flow', loader=load_directed_flow_graph, times=1)
def run(G):
    rg = residual_graph(G)
    s, t = 1, G.V - 1
    return max_flow(rg, s, t)