from random import randint
from itertools import accumulate


class Solution:

    def __init__(self, w: list[int]):
        self.left = list(accumulate(w, initial=0))
        self.total = self.left[-1]

    def pickIndex(self) -> int:
        if len(self.left) == 2:  # only 1 element in w
            return 0

        r = randint(0, self.total - 1)
        i = self.max_i_geq_t(r)
        return i

    def max_i_geq_t(self, t):
        lo = 0
        hi = len(self.left)
        while lo < hi:
            mid = (lo + hi) // 2
            if self.left[mid] > t:
                hi = mid
            else:
                lo = mid + 1
        return lo - 1


obj = Solution([1, 3])
param_1 = obj.pickIndex()
print(param_1)
