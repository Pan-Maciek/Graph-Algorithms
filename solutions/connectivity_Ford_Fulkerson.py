from test_utils import test, load_graph

from algorithms.max_flow.ford_fulkerson import max_flow

# Finding edge connectivity in undirected graph using Ford-Fulkerson's method

@test(data='./data/lab2/connectivity', loader=load_graph)
def run(G):
    s, t = min(range(1, G.V), key=G.edges_count), G.V - 1
    return max_flow(G, s, t)