from test_utils import test, load_flow_graph

from algorithms.max_flow.ford_fulkerson import max_flow
from structures.graph import residual_graph, flow_edge

# Finding edge connectivity in undirected graph using Ford-Fulkerson's method

@test(data='./data/lab2/connectivity', loader=load_flow_graph, times=1)
def run(G):
    rg, s = residual_graph(G), 1
    def connectivity(t):
        rg.clear(flow_edge.reset_flow)
        return max_flow(rg, s, t)

    return min(connectivity(t) for t in range(1, G.V) if s != t)