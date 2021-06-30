from typing import List
from functools import cache


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)  # number of solutions, index as amount
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i-coin]
        return dp[amount]


# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         @cache
#         def f(t):
#             if t == 0:
#                 return 1
#             return sum((f(t-coin) for coin in coins if t-coin >= 0))
#         return f(amount)

x = Solution()
ans = x.change(3,  [2, 1])
print(ans)