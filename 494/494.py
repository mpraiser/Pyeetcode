import functools
from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ans = 0
        if (tmp := target + sum(nums)) % 2 != 0:
            return 0 
        indirect_target = tmp // 2

        # problem converted to: sum(c) == indirect_target
        # c is a sub array
        @functools.cache
        def helper(i, psum):
            """
            number of first i-th elements whose sum is psum
            """
            if i == 0:
                return 1 if psum == 0 else 0
            ans = helper(i - 1, psum)
            if psum >= nums[i-1]:
                ans += helper(i - 1, psum - nums[i-1])
            return ans
            
        # def helper(i, psum):
        #     nonlocal ans
        #     if i < len(nums):
        #         if psum > indirect_target:
        #             return
        #         helper(i + 1, psum + nums[i])
        #         helper(i + 1, psum)
        #     else:
        #         if psum == indirect_target:
        #             ans += 1
        # helper(0, 0)

        return helper(len(nums), indirect_target)
        

x = Solution()
ans = x.findTargetSumWays([1,1,1,1,1], 3)
# ans = x.findTargetSumWays([1], 1)
print(ans)