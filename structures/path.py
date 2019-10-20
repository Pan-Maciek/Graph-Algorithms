class path(tuple):
    def __new__(self, iter):
        return tuple.__new__(path, iter)

    def __str__(self):
        return '(' + ' -> '.join(map(str, self)) + ')'

    @staticmethod
    def from_previous_list(previous, index):
        reversed_path = []
        while previous[index] != None:
            reversed_path.append(index)
            index = previous[index]
        reversed_path.append(index)
        return path(reversed(reversed_path))