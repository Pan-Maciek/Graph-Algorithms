from test_utils import test, load_graph
from algorithms.paths.dijkstra import dijkstra_paths, high_priority, inf, Relax, SkipRelaxation, dijkstra

# Finding path with max flow using modified Dijkstra's algorithm

def relax(u, v, w):
    flow = min(u, w)
    return Relax(flow) if flow > v else SkipRelaxation

s, t = 1, 2
@test(data="./data/lab1", loader=load_graph)
def run(G):
    paths = dijkstra_paths(G, s, initial_distance=0, source_distance=inf, relax=relax, priority=high_priority)
    max_flow_path = paths(t)
    max_flow = max_flow_path.accumulated
    return max_flow
