from typing import List, Tuple
from functools import cache


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        @cache
        def helper(s: Tuple) -> int:
            """
            best weight
            """
            if len(s) <= 2:
                if len(s) == 0:
                    return 0
                if len(s) == 1:
                    return s[0]
                if len(s) == 2:
                    return abs(s[0] - s[1])    
            
            # len(s) >= 3, keep search
            solutions = []
            # pick two nums
            for i in range(len(s) - 1):
                for j in range(i + 1, len(s)):
                    if s[i] > s[j]:
                        next_s = (s[m] if m != i else s[i] - s[j] for m in range(len(s)) if m != j)
                    elif s[i] < s[j]:
                        next_s = (s[m] if m != j else s[j] - s[i] for m in range(len(s)) if m != i)
                    else:
                        next_s = (s[m] for m in range(len(s)) if m !=i and m != j)
                    
                    weight = helper(tuple(next_s))
                    if weight == 0:
                        return 0
                    solutions.append(weight)
            return min(solutions)
        
        return helper(tuple(stones))



x = Solution()
# ans = x.lastStoneWeightII([2,7,4,1,8,1])
ans = x.lastStoneWeightII([31,26,33,21,40])
# ans = x.lastStoneWeightII([1,2])
# ans = x.lastStoneWeightII([1,1,2,3,5,8,13,21,34,55,89,14,23,37,61,98])
print(ans)