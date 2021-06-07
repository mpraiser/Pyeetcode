from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ans = 0
        if (tmp := target + sum(nums)) % 2 != 0:
            return 0 
        indirect_target = tmp // 2

        # problem converted to: sum(c) == indirect_target
        # c is a sub array
        nums.sort(reverse=True)
        def helper(i, psum):
            nonlocal ans
            if i < len(nums):
                if psum > indirect_target:
                    return
                helper(i + 1, psum + nums[i])
                helper(i + 1, psum)
            else:
                if psum == indirect_target:
                    ans += 1
        helper(0, 0)
        return ans
        

x = Solution()
ans = x.findTargetSumWays([1,1,1,1,1], 3)
# ans = x.findTargetSumWays([1], 1)
print(ans)