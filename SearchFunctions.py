# SearchFunctions.py
# Iterative binary-search style "lower_bound":
# returns the first index i such that arr[i] >= target; or len(arr) if none.

from typing import List

def lower_bound(arr: List[int], target: int) -> int:
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo
