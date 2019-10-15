from structures.graph import numeric_graph, weight
from algorithms.search.binary_search import binary_search, SelectAndMore, Less
from algorithms.search.dfs import dfs
from test_utils import test, load_graph

# Finding max flow using binary search

s, t = 1, 2

@test(data="./data", loader=load_graph)
def run(G):

  def find_max_flow(flow):
      return SelectAndMore(flow) if dfs(G, s, t, condition=lambda edge: weight(edge) >= flow) else Less

  max_flow = binary_search(map(weight, G.E), find_max_flow)
  return max_flow