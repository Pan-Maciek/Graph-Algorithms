from copy import copy

class graph(object):
    def __init__(self, V, E, directed=True):
        self.V = V
        self._vert_info = [[] for _ in range(V)]
        self.E = E
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
        self.V = base_graph.V
        self._directed = base_graph._directed
        self.weight = list([None for _ in range(base_graph.V)] for _ in range(base_graph.V))
        self._data = list([] for _ in range(base_graph.V))
        if base_graph._directed:
            for u, v, w in base_graph.E:
                self.weight[u][v] = w
                self._data[u].append(v)
        else:
            for u, v, w in base_graph.E:
                self.weight[u][v] = w
                self.weight[v][u] = w
                self._data[u].append(v)
                self._data[v].append(u)
    
    def edges(self, u):
        return ((v, self.weight[u][v]) for v in self._data[u])
    
    def neighbors(self, u):
        return iter(self._data[u])

    def inc_weight(self, u, v, delta):
        if self.weight[u][v] == None:
            self.weight[u][v] = delta
            self._data[u].append(v)
        else:
            self.weight[u][v] = self.weight[u][v] + delta

    def dec_weight(self, u, v, delta):
        self.inc_weight(u, v, -delta)

def weight(edge):
    return edge[-1]

def min_weight(min_weight, strong=False):
    return (lambda edge: weight(edge) > min_weight) if strong else (lambda edge: weight(edge) >= min_weight)