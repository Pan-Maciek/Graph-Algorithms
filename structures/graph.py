from copy import copy

class graph(object):
    def __init__(self, V, E, directed=True):
        self.V = V
        self._vert_info = [[] for _ in range(V)]
        self.E = E
        self._directed = directed
        for edge in E:
            u, v, w  = edge
            self._vert_info[u].append(edge)
            if not directed:
                self._vert_info[v].append((v, u, copy(w)))
        
    def edges(self, u):
        return self._vert_info[u]
    
    def neighbors(self, u):
        return (v for _, v, _ in self._vert_info[u])

class residual_graph(object):
    def __init__(self, base_graph):
        self.V = V = base_graph.V

        self._vert_info = [[] for _ in range(V)]
        self._edge_info = [[None for _ in range(V)] for _ in range(V)]
        self._directed = base_graph._directed

        if base_graph._directed:
            for u, v, w in base_graph.E:
                self._edge_info[u][v] = (u, v, w)
                self._vert_info[u].append(v)
        else:
            for u, v, w in base_graph.E:
                self._edge_info[u][v] = (u, v, w)
                self._edge_info[v][u] = (v, u, copy(w))
                self._vert_info[u].append(v)
                self._vert_info[v].append(u)
    
    def edges(self, u):
        return (self._edge_info[u][v] for v in self._vert_info[u])
    
    def edge(self, u, v, default_info=None):
        if self._edge_info[u][v] == None:
            if default_info == None:
                return None
            self._vert_info[u].append(v)
            self._edge_info[u][v] = (u, v, default_info)
        return self._edge_info[u][v][2]

    def neighbors(self, u):
        return iter(self._vert_info[u])

    def update_edge(self, u, v, w):
        if self._vert_info[u][v] == None:
            self._vert_info[u].append(v)
        self._edge_info[u][v] = (u, v, w)

def weight(edge):
    return edge[-1]

def min_weight(min_weight, strong=False):
    return (lambda edge: weight(edge) > min_weight) if strong else (lambda edge: weight(edge) >= min_weight)

class flow_edge(object):
    def __init__(self, w):
        self.flow = 0
        self.capacity = w

    @staticmethod
    def not_saturated(edge):
        return edge[2].capacity > edge[2].flow
