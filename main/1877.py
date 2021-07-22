from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return max(
                (nums[i] + nums[-1-i] for i in range(len(nums)//2))
            )


ans = Solution().minPairSum([3,5,4,2,4,6])
print(ans)