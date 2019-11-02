from test_utils import test, load_graph
from structures.graph import weight
from structures.disjoint_set import numeric_disjoint_set

# Finding path with max flow using disjoint sets

s, t = 1, 2
@test(data='./data/lab1', loader=load_graph)
def run(G):
    S = numeric_disjoint_set(G.V)
    max_flow = None
    for u, v, w in sorted(G.E, key=weight, reverse=True): 
        S.union(u, v) 

        if S.find(s) == S.find(t): 
            max_flow = w
            break
    return max_flow
