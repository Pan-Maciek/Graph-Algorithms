from collections import deque

class path(tuple):
    def __new__(self, iter, accumulated=None):
        return tuple.__new__(path, iter)

    def __init__(self, iter, accumulated=None):
        self.accumulated = accumulated

    def __str__(self):
        return ('(' if self.accumulated == None else '(acc: ' + str(self.accumulated) + '; ') + ' -> '.join(map(str, tuple.__iter__(self))) + ')' 

    def __iter__(self):
        if bool(self):
            iterable = tuple.__iter__(self) 
            u = next(iterable)
            
            for v in iterable:
                yield u, v
                u = v

    @staticmethod
    def from_previous_list(previous, index, accumulator=None, initial_acc_state=0):
        _path = deque()
        state = initial_acc_state
        if previous[index] == None:
            return None
        if accumulator == None:
            while previous[index] != None:
                _path.appendleft(index)
                index, _, _ = previous[index]
            _path.appendleft(index)
        else:
            while previous[index] != None:
                _path.appendleft(index)
                index, _, w = previous[index]
                state = accumulator(state, w)
            _path.appendleft(index)
        return path(_path, accumulated = None if accumulator == None else state)

def sum_along_path(a, b):
    return a + b

def min_along_path(a, b):
    return a if a < b else b

def min_bandwidth(old, w):
    return min(old, w.capacity - w.flow)