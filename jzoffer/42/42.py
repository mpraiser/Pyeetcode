from typing import List, Tuple
from functools import cache


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        @cache
        def f(n) -> int:
            """biggest sum of sub array ends with nums[n-1]"""
            if n == 1:
                return nums[0]
            else:
                if f(n-1) <= 0:
                    return nums[n-1]
                else:
                    return f(n-1) + nums[n-1]

        return max((f(i) for i in range(1, len(nums)+1)))

ans = Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(ans)