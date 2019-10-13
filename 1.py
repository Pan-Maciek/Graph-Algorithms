from structures.graph import numeric_graph, weight
from algorithms.search.binary_search import binary_search, MarkAndMore, Less
from algorithms.search.dfs import dfs

# Finding max flow using binary search

G = numeric_graph.load('./data/grid100x100', directed=False)
s, t = 1, 2

def find_max_flow(flow):
    return MarkAndMore if dfs(G, s, t, condition=lambda edge: weight(edge) >= flow) else Less

max_flow = binary_search(map(weight, G.E), find_max_flow)

print(max_flow)
