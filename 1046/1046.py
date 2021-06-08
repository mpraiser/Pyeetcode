from typing import List, Tuple


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
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

            # pick two nums

            if s[0] >= s[1]:
                max_1st = s[0]
                max_1st_p = 0
                max_2nd = s[1]
                max_2nd_p = 1
            else:
                max_1st = s[1]
                max_1st_p = 1
                max_2nd = s[0]
                max_2nd_p = 0
            for i in range(2, len(s)):
                if s[i] > max_1st:
                    max_2nd = max_1st
                    max_2nd_p = max_1st_p
                    max_1st = s[i]
                    max_1st_p = i
                elif s[i] > max_2nd:
                    max_2nd = s[i]
                    max_2nd_p = i



            if max_1st != max_2nd:
                next_s = (s[m] if m != max_1st_p else max_1st - max_2nd for m in range(len(s)) if m != max_2nd_p)
            else:
                next_s = (s[m] for m in range(len(s)) if m != max_1st_p and m != max_2nd_p)
                    
            return helper(tuple(next_s))
        return helper(tuple(stones))

x = Solution()
ans = x.lastStoneWeight([2,7,4,1,8,1])
# ans = x.lastStoneWeight([31,26,33,21,40])
print(ans)