from test_utils import test, load_flow_graph

from algorithms.max_flow.ford_fulkerson import max_flow

# Finding edge connectivity in undirected graph using Ford-Fulkerson's method

@test(data='./data/lab2/connectivity', loader=load_flow_graph, times=1)
def run(G):
    s = 1
    return min((max_flow(G, s, t) for t in range(2, G.V - 1)))