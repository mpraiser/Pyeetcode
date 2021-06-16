from typing import List
from functools import cache


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @cache
        def f(i, j):
            """
            delta of stones in [i, j), j >= i+1
            """

            if j == i+2:
                return abs(piles[i] - piles[j-1])
            
            return max(
                f(i+2, j) + piles[i] - piles[i+1], 
                f(i+1, j-1) + piles[i] - piles[j-1],
                f(i+1, j-1) - piles[i] + piles[j-1],
                f(i, j-2), - piles[j-2] + piles[j-1])
        
        return f(0, len(piles)) > 0


ans = Solution().stoneGame([3,2,10,4])
print(ans)