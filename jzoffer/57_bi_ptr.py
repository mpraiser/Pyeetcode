from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1
        while i < j:
            s = nums[i] + nums[j]
            if s == target:
                return [nums[i], nums[j]]
            elif s > target:
                j -= 1
            elif s < target:
                i += 1

            
ans = Solution().twoSum([2,7,11,15], 9)
print(ans)