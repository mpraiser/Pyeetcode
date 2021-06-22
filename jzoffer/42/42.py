from typing import List, Tuple
from functools import cache


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]]
        for i in range(1, len(nums)):
            if dp[i-1] <= 0:
                dp.append(nums[i])
            else:
                dp.append(nums[i] + dp[i-1])
        return max(dp)

ans = Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(ans)