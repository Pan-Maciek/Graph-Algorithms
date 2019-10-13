from structures.graph import numeric_graph, weight
from structures.disjoint_set import numeric_disjoint_set

# Finding max flow using disjoint sets

G = numeric_graph.load('./data/grid100x100', directed=False)
S = numeric_disjoint_set(G.V)
s, t = 1, 2

max_flow = None
for (u, v, w) in sorted(G.E, key=weight, reverse=True):
    S.union(u, v)

    if S.find(s) == S.find(t):
        max_flow = w
        break

print(max_flow)
