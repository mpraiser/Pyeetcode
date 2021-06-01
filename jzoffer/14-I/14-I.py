from functools import cache

@cache
def max_product(n: int) -> int:
    """
    Args:
        n: n >= 0
    """
    if n >= 3:
        # the first divide cannot split
        return max((i * max_product_split(n-i) for i in range(1, n//2+1)))
    else:
        return 1

@cache
def max_product_split(n: int) -> int:
    # special case i == 0:
    # in this case, do not split n into two halves
    return max((i * max_product_split(n-i) if i != 0 else n for i in range(n//2+1)))


class Solution:
    def cuttingRope(self, n: int) -> int:
        return max_product(n)


x = Solution()
ans = x.cuttingRope(3)
print(ans)