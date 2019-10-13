from itertools import count

class numeric_disjoint_set(object):
    class subset(object):
        def __init__(self, parent):
            self.parent = parent
            self.rank = 0

    def __init__(self, size):
        self._data = [numeric_disjoint_set.subset(i) for i in range(size)]

    def find(self, u):
        if u != self._data[u].parent:
            self._data[u].parent = self.find(self._data[u].parent)
        return self._data[u].parent

    def union(self, u, v):
        u_rep, v_rep = self.find(u), self.find(v)
        u_rank, v_rank = self._data[u_rep].rank, self._data[v_rep].rank

        if u_rank < v_rank:
            self._data[u_rep].parent = v_rep
            return v_rep
        elif v_rank < u_rank:
            self._data[v_rep].parent = u_rep
            return u_rep
        else:
            self._data[u_rep].parent = v_rep
            self._data[v_rep].rank = self._data[v_rep].rank + 1
            return v_rep


class disjoint_set(object):
    def __init__(self, iterable):
        self._dict = dict(zip(iterable, count()))
        self._numeric = numeric_disjoint_set(len(self._dict))

    def find(self, u):
        return self._numeric.find(self._dict[u])

    def union(self, u, v):
        return self._numeric.union(self._dict[u], self._dict[v])