class edge(tuple):
    def __new__(self, u, v):
        t = u, v
        return tuple.__new__(edge, (min(t), max(t)))

    def __eq__(self, other):
        return self[0] == other[0] and self[1] == other[1]

    def __hash__(self):
        return tuple.__hash__(self)

    def __str__(self):
        return f"{{{self[0]}, {self[1]}}}"

class arch(tuple):
    def __new__(self, u, v):
        return tuple.__new__(arch, (u, v))

    def __eq__(self, other):
        return self[0] == other[0] and self[1] == other[1]

    def __hash__(self):
        return tuple.__hash__(self)

    def __str__(self):
        return f"({self[0]}, {self[1]})"

class graph(object):

    def __init__(self, V={}, A={}, E={}, **kwargs):
        self.V = V
        self._directed = len(A) > 0
        self.A = {arch(u, v) for u, v in A}
        self.E = {edge(u, v) for u, v in E}

        self._graph = dict((v, set()) for v in V)
        for key in V:
            s = self._graph[key]
            for u, v in A:
                if key == u:
                    s.add(v)
            for u, v in E:
                if key == u:
                    s.add(v)
                    self._graph[v].add(key)
                elif key == v:
                    s.add(u)
                    self._graph[u].add(key)


    def neighbors_of(self, s):
        for key in self._graph[s]:
            yield key

    def edges_of(self, s):
        return (e for e in self.E if s in e)

    def arches_of(self, s):
        return (a for a in self.A if a[0] == s)

    def __iter__(self):
        for vert in self.V:
            yield vert

    def __str__(self):
        V = ", ".join(map(str, self.V))
        E = ", ".join(map(str, self.E))
        A = ", ".join(map(str, self.A))
        return f"(V: {{{V}}}, A: {{{A}}})" if self._directed else f"(V: {{{V}}}, E: {{{E}}})"

