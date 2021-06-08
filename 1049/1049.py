from typing import List, Tuple
from functools import cache


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        @cache
        def helper(s: Tuple) -> int:
            """
            best weight
            """
            if len(s) == 0:
                return 0
            if len(s) == 1:
                return s[0]
            
            solutions = []
            # len(s) >= 2, keep search
            for i in range(len(s) - 1):
                for j in range(i + 1, len(s)):
                    next_s = [s[m] for m in range(len(s)) if m != i and m != j]
                    if s[i] != s[j]:
                        next_s.append(abs(s[i] - s[j]))
                    solutions.append(helper(tuple(next_s)))
            return min(solutions)
        
        return helper(tuple(stones))



x = Solution()
# ans = x.lastStoneWeightII([2,7,4,1,8,1])
# ans = x.lastStoneWeightII([31,26,33,21,40])
# ans = x.lastStoneWeightII([1,2])
ans = x.lastStoneWeightII([1,1,2,3,5,8,13,21,34,55,89,14,23,37,61,98])
print(ans)