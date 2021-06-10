from typing import List
from functools import cache


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def f(i, t):
            """
            return numbers of solutions selecting in first i-th coins whose sum is t
            t <= amount
            """
            if i == 1:
                return 1 if t % coins[i-1] == 0 else 0
            # how many new coins are selected
            ans = 0
            n = 0
            while (s_n := n * coins[i-1]) <= t:
                ans += f(i-1, t - s_n)
                n += 1
            return ans
        return f(len(coins), amount)

x = Solution()
ans = x.change(3,  [2])
print(ans)