import random
from typing import List, get_type_hints


def qselect(s: List, k: int, *, reverse=False):
    """
    Args:
        s: list
        k: k in [1, len(s)]
        reverse: if True, from big -> small
    """
    if len(s) == 1:
        return s[0]
    
    if not (1 <= k <= len(s)):
        raise Exception('k out of bound.')

    pivot = random.choice(s)
    if reverse:
        left = [x for x in s if x > pivot]
        mid = [x for x in s if x == pivot]
        right = [x for x in s if x < pivot]
    else:
        left = [x for x in s if x < pivot]
        mid = [x for x in s if x == pivot]
        right = [x for x in s if x > pivot]

    if k <= len(left):
        return qselect(left, k, reverse=reverse)
    elif k <= len(left) + len(mid):
        return pivot
    else:
        j = k - len(left) - len(mid)
        return qselect(right, j, reverse=reverse)


def qselect_inplace(s: List, k, lo=None, hi=None, *, key=None, reverse=False):
    """
    return k-th in [ptr_l, ptr_r)
    """
    if not lo:
        lo = 0
    if not hi:
        hi = len(s)

    if lo > hi:
        return None
    elif lo == hi:
        return s[lo]

    if not (1 <= k <= hi - lo + 1):
        raise Exception('k out of boundary')

    # index of pivot
    p = random.randint(lo, hi-1)

    # put pivot to the end of list
    s[hi-1], s[p] = s[p], s[hi-1]
    
    i = j = lo
    # i: number of elements bigger than pivot
    # select elements bigger than pivot
    while j < hi-1:
        if not key:
            key = lambda x: x
        cmp = key(s[j]) < key(s[hi-1])
        if reverse:
            cmp = not (cmp)
        if cmp:
            s[i], s[j] = s[j], s[i]
            i += 1
        j += 1

    # get back the pivot
    s[i], s[hi-1] = s[hi-1], s[i]
    p = i

    if lo + (k-1) < p:
        return qselect_inplace(s, k, lo, p, reverse=reverse)
    elif lo + (k-1) == p:
        return s[p]
    else:
        return qselect_inplace(s, k-(p-lo+1), p+1, reverse=reverse)


if __name__ == "__main__":
    s = [("a", 1), ("c", 3), ("fff", 666), ("b", 2)]
    k = 2
    ans = qselect_inplace(s, k, key=lambda x: x[1], reverse=True)
    print(ans)

    print(s)