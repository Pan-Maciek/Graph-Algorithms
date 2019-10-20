from test_utils import test, load_graph

from structures.graph import weight, min_weight
from algorithms.search.binary_search import SelectAndMore, Less, binary_search
from algorithms.paths.bfs import bfs_path
from algorithms.numeric.min_max import min_max

# Finding path with max flow using binary search

s, t = 1, 2

@test(data="./data/lab1", loader=load_graph)
def run(G):
    def find_max_flow(flow):
        path = bfs_path(G, s, t, condition=min_weight(flow))
        return SelectAndMore((flow, path)) if path != None else Less
  
    min, max = min_max(map(weight, G.E))
    max_flow, path = binary_search(min, max, find_max_flow)
    return max_flow