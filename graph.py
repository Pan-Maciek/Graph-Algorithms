from itertools import chain
class edge(tuple):
    def __new__(self, u, v):
        return tuple.__new__(edge, sorted((u, v)))

    def __str__(self):
        return f"{{{self[0]}, {self[1]}}}"

class arc(tuple):
    def __new__(self, u, v):
        return tuple.__new__(arc, (u, v))

    def __str__(self):
        return f"({self[0]}, {self[1]})"

class path(tuple):
    def __eq__(self, other):
        for u, v in zip(self, other):
            if u != v: 
                return False
        return True

    def __hash__(self):
        return tuple.__hash__(self)
    
    def __str__(self):
        s = " -> ".join(self)
        return f"({s})"

class graph(dict):
    def __init__(self, init, directed=True):
        self.directed = directed
        super(graph, self).__init__(init)

    def neighbors_of(self, s):
        return self[s]

    def edges_of(self, s):
        return {edge(s, t) for t in self[s]}

    def arcs_of(self, s):
        return {arc(s, t) for t in self[s]}

    def __add__(self, other):
        return graph((key, self.get(key, set()).copy().union(other.get(key, set()).copy())) for key in chain(self, other))

def not_visited(visited, iter):
  return (v for v in iter if v not in visited)