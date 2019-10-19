from test_utils import test, load_graph

from structures.graph import weight
from algorithms.search.binary_search import SelectAndMore, Less, binary_search
from algorithms.search.bfs import bfs
from algorithms.numeric.min_max import min_max

# Finding path with max flow using binary search

s, t = 1, 2

@test(data="./data/lab1", loader=load_graph)
def run(G):
  def find_max_flow(flow):
      return SelectAndMore(flow) if bfs(G, s, t, condition=lambda edge: weight(edge) >= flow) else Less
  
  min, max = min_max(map(weight, G.E)) # O(n)
  max_flow = binary_search(min, max, find_max_flow) # O(logn(|V|+|E|+1)) where n = max - min
  return max_flow