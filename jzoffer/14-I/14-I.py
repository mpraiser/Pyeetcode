from itertools import chain
from functools import cache

@cache
def max_product(n: int) -> int:
    """
    Args:
        n: n >= 0
    """
    if n >= 2:
        # the first divide cannot split
        return max(
            chain(
                (i * (n-i) for i in range(1, n//2+1)),
                (i * max_product(n-i) for i in range(1, n//2+1))
                )
            )
    else:
        return 0


class Solution:
    def cuttingRope(self, n: int) -> int:
        return max_product(n)


x = Solution()
ans = x.cuttingRope(10)
print(ans)