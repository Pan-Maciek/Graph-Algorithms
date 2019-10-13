NotFound = None
Found = 0
More, Less = 1, -1
MarkAndMore, MarkAndLess = 2, -2

__sorted = sorted  # Used because of argument name

def binary_search(iterable, action, sorted=False):
    iterable = list(iterable) if sorted else list(__sorted(iterable))
    L, R = 0, len(iterable)
    mark = -1

    while(L <= R):
        m = (L + R) // 2
        sgn = action(iterable[m])
        if sgn == NotFound: return NotFound
        elif sgn == Found: return iterable[m]
        elif sgn == More: L = m + 1
        elif sgn == Less: R = m - 1
        elif sgn == MarkAndMore:
          mark = m
          L = m + 1
        elif sgn == MarkAndLess:
          mark = m
          R = m - 1

    return iterable[mark] if mark != -1 else NotFound
