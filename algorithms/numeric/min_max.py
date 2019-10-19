def min_max(iterable):
    """
    Get min and max in O(n)
    """
    iterator = iter(iterable)
    min = max = next(iterator)
    for val in iterator:
        if val > max:
            max = val
        elif val < min:
            min = val
    return min, max