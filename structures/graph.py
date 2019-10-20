class numeric_graph(object):
    def __init__(self, V, E, directed=True):
        self.V = V
        self.E = E
        self._data = list([] for _ in range(V))
        self._directed = directed
        if directed:
            for u, v, w in E:
                self._data[u].append((v, w))
        else:
            for u, v, w in E:
                self._data[u].append((v, w))
                self._data[v].append((u, w))

    def edges(self, u):
        for v in self._data[u]:
            yield v

    def neighbors(self, u):
        for v, _ in self._data[u]:
            yield v

    @staticmethod
    def load(path, directed=True):
        V = 0
        L = []
        f = open(path, 'r')
        for l in f.readlines():
            s = l.split()
            if len(s) < 1 or s[0] == 'c':
                continue
            elif s[0] == 'p':
                V = int(s[2]) + 1
            elif s[0] == 'e':
                (x, y, c) = (int(s[1]), int(s[2]), int(s[3]))
                # (x, y) = (min(a, b), max(a, b))
                L.append((x, y, c))
        f.close()
        return numeric_graph(V, L, directed=directed)

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
    return lambda edge: weight(edge) > min_weight if strong else lambda edge: weight(edge) >= min_weight