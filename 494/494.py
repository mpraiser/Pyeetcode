from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ans = 0

        def helper(i, psum):
            nonlocal ans
            if i < len(nums):
                helper(i + 1, psum + nums[i])
                helper(i + 1, psum - nums[i])
            else:
                if psum == target:
                    ans += 1

        helper(0, 0)
        return ans


x = Solution()
ans = x.findTargetSumWays([1,1,1,1,1], 3)
print(ans)