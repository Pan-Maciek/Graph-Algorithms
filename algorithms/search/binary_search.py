Found, NotFound = 0, None
More, Less = 1, -1
def SelectAndMore(val):
  return (More, val)
def SelectAndLess(val):
  return (Less, val)

__sorted = sorted  # Used because of argument name

def binary_search(min, max, selector):
    """
    Used for values from "continuous" range of integers from [min, max]  
    Time complexity of this function depends on range [min, max] range.  
    O(slogn) where n = max - min and s is time complexity of selector
    """
    L, R = min, max
    selected = None

    while L <= R:
        m = (L + R) // 2
        action = selector(m)
        if action == NotFound: return NotFound
        elif action == Found: return m
        elif action == More: L = m + 1
        elif action == Less: R = m - 1
        elif action[0] == More:
          selected = action[1]
          L = m + 1
        elif action[0] == Less:
          selected = action[1]
          R = m - 1

    return selected

def discrete_binary_search(iterable, selector, sorted=False):
    """
    Used for discrete values from given set.  
    Generally O((s+n)logn) where s is time complexity of selector
    O(n+nlogn+slogn) if sorted=False  
    O(n+slogn) if sorted=True  
    O(slogn) if sorted=True and iterable is list  
    """
    if isinstance(iterable, list):
        iterable = iterable if sorted else list(__sorted(iterable))
    else:
        iterable = list(iterable) if sorted else list(__sorted(iterable))

    L, R = 0, len(iterable) - 1
    selected = None

    while L <= R:
        m = (L + R) // 2
        action = selector(iterable[m])
        if action == NotFound: return NotFound
        elif action == Found: return iterable[m]
        elif action == More: L = m + 1
        elif action == Less: R = m - 1
        elif action[0] == More:
          selected = action[1]
          L = m + 1
        elif action[0] == Less:
          selected = action[1]
          R = m - 1

    return selected
