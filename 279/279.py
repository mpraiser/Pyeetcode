from math import sqrt, ceil
from functools import cache


class Solution:
    def numSquares(self, n: int) -> int:

        @cache
        def f(n):
            """
            1 <= n <= 10 ** 4
            """
            if n <= 3:
                return n
            # if n is square itself
            if sqrt(n) % 1 == 0:
                return 1
            return min(
                (f(n - i**2) + 1 for i in reversed(range(1, ceil(sqrt(n)))))
            )

        return f(n)


x = Solution()
# ans = x.numSquares(12)
ans = x.numSquares(13)
print(ans)