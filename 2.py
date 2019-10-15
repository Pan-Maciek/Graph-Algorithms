from structures.graph import numeric_graph, weight
from structures.disjoint_set import numeric_disjoint_set
from test_utils import test, load_graph

# Finding max flow using disjoint sets

@test(data='data', loader=load_graph)
def run(G):
    S = numeric_disjoint_set(G.V)
    s, t = 1, 2
    max_flow = None
    for (u, v, w) in sorted(G.E, key=weight, reverse=True):
        S.union(u, v)

        if S.find(s) == S.find(t):
            max_flow = w
            break
    return max_flow
