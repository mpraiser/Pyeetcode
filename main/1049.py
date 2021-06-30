from typing import List, Tuple
from functools import cache


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        @cache
        def f(i, t):
            """
            Args:
                i: first i-th stones
                t: constraint, max sum
            Returns:
                max sum in first i-th stones, which is less than t
            """
            if i == 0:
                return 0
            ans = f(i-1, t)
            if t >= stones[i-1]:
                ans = max(ans, f(i-1, t-stones[i-1]) + stones[i-1])
            return ans
        return total - 2 * f(len(stones), total/2)



x = Solution()
# ans = x.lastStoneWeightII([2,7,4,1,8,1])
# ans = x.lastStoneWeightII([31,26,33,21,40])
ans = x.lastStoneWeightII([1,1,4,2,2])
# ans = x.lastStoneWeightII([1,1,2,3,5,8,13,21,34,55,89,14,23,37,61,98])
print(ans)