from test_utils import test, load_directed_graph

from algorithms.max_flow.ford_fulkerson import max_flow

# Finding max flow in network using Ford-Fulkerson's method + dfs

@test(data='./data/lab2/flow', loader=load_directed_graph, times=1)
def run(G):
    s, t = 1, G.V - 1
    return max_flow(G, s, t)