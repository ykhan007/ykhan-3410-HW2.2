# SortFunctions.py
# Iterative quicksort with a key= function.
# We’ll pass key=lambda p: p[0][0] so it sorts by the RED value of ((r,g,b),(x,y)).

from typing import List, Callable, Any, Optional

def quicksort_iterative(a: List[Any], key: Optional[Callable[[Any], Any]] = None) -> None:
    
    if len(a) <= 1:
        return

    def kval(v):  # local helper for key lookup
        return v if key is None else key(v)

    def partition(lo: int, hi: int) -> int:
        # median-of-three-ish: pick mid to reduce worst-cases on presorted data
        mid = (lo + hi) // 2
        pivot = kval(a[mid])
        i, j = lo, hi
        while True:
            while kval(a[i]) < pivot:
                i += 1
            while kval(a[j]) > pivot:
                j -= 1
            if i >= j:
                return j
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1

    stack = [(0, len(a) - 1)]
    while stack:
        lo, hi = stack.pop()
        if lo >= hi:
            continue
        p = partition(lo, hi)
        # push larger segment first to keep stack shallow
        if (p - lo) > (hi - (p + 1)):
            stack.append((lo, p))
            stack.append((p + 1, hi))
        else:
            stack.append((p + 1, hi))
            stack.append((lo, p))
