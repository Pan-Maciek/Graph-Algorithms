def min_max(iterable):
    iterator = iter(iterable)
    min = max = next(iterator)
    for val in iterator:
        if val > max:
            max = val
        elif val < min:
            min = val
    return min, max