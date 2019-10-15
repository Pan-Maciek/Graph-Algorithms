class numeric_graph(object):
    def __init__(self, V, E, directed=True):
        self.V = V
        self.E = E
        self._data = list([] for _ in range(V))
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


def weight(edge):
    return edge[-1]
