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
        reversed_path = []
        state = initial_acc_state
        if previous[index] == None:
            return None
        if accumulator == None:
            while previous[index] != None:
                reversed_path.append(index)
                index, _ = previous[index]
            reversed_path.append(index)
        else:
            while previous[index] != None:
                reversed_path.append(index)
                index, w = previous[index]
                state = accumulator(state, w)
            reversed_path.append(index)
        return path(reversed(reversed_path), accumulated = None if accumulator == None else state)

def sum_along_path(a, b):
    return a + b

def min_along_path(a, b):
    return a if a < b else b