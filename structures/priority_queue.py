def high_priority(a, b):
    return a > b

def low_priority(a, b):
    return a < b

def swap(array, a, b):
    array[a], array[b] = array[b], array[a]

def heapify(array, i, N, cmp=high_priority, swap=swap):
    while True:
        L, R = 2 * i + 1, 2 * i + 2
        S = i  # selected
        if L < N and cmp(array[L], array[S]): S = L
        if R < N and cmp(array[R], array[S]): S = R
        if S != i:
            swap(array, i, S)
            i = S
        else: break

def build_heap(array, i, N, cmp=high_priority):
    for i in range(N // 2, -1, -1):
        heapify(array, i, N, cmp=cmp)

def sift_up(array, i, cmp=high_priority, swap=swap):
    while i > 0 and cmp(array[i], array[(i - 1) // 2]):
        parent = (i - 1) // 2
        swap(array, i, parent)
        i = parent

class priority_queue(object):

    class priority_info():
        def __init__(self, priority, index):
            self.priority = priority
            self.index = index

        def __str__(self):
            p, i = self.priority, self.index
            return f"(p: {p}, i: {i})"

    def __init__(self, max_size, priority=high_priority):
        self._max_size = max_size
        self.size = 0
        self._keys = [None for _ in range(max_size)]
        self._info = dict()
        self._raw_priority = priority
        def _priority(a, b):
            return priority(self._info[a].priority, self._info[b].priority)
        self._priority = _priority
        def swap(keys, a, b):
            keys[a], keys[b] = keys[b], keys[a]
            self._info[keys[a]].index, self._info[keys[b]].index = self._info[keys[b]].index, self._info[keys[a]].index
        self._swap = swap

    def push(self, key, priority):
        if key in self._info:
            raise KeyError("All keys must be unique")
        self._push(key, priority)

    def _push(self, key, priority):  # skip uniq key check
        self._keys[self.size] = key
        self._info[key] = priority_queue.priority_info(priority, self.size)
        sift_up(self._keys, self.size, cmp=self._priority, swap=self._swap)
        self.size += 1

    def pop(self):
        key = self._keys[0]
        priority = self._info[key].priority
        del self._info[key]
        self.size -= 1
        if self.size != 0:
            self._keys[0] = self._keys[self.size]
            self._keys[self.size] = None
            self._info[self._keys[0]].index = 0
            heapify(self._keys, 0, self.size, self._priority, swap=self._swap)
        return (key, priority)

    def change_priority(self, key, priority):
        old_priority = self._info[key].priority
        self._info[key].priority = priority
        if self._raw_priority(priority, old_priority): #?
            sift_up(self._keys, self._info[key].index, cmp=self._priority, swap=self._swap)
        else:
            heapify(self._keys, self._info[key].index, self.size, cmp=self._priority, swap=self._swap)

    def extend(self, iter):
        for key, priority in iter:
            self.push(key, priority)

    def mutable_iter(self):
        while self.size != 0:
            yield self.pop()