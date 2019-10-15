Found, NotFound = 0, None
More, Less = 1, -1
def SelectAndMore(val):
  return (More, val)
def SelectAndLess(val):
  return (Less, val)

__sorted = sorted  # Used because of argument name

def binary_search(iterable, selector, sorted=False):
    iterable = list(iterable) if sorted else list(__sorted(iterable))
    L, R = 0, len(iterable) - 1
    selected = None

    while(L <= R):
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
