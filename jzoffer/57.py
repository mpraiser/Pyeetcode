from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1, 0, -1):
            if nums[i] < target:
                for j in range(i):
                    tmp = nums[i] + nums[j]
                    if tmp > target:
                        break
                    elif tmp == target:
                        return [nums[i], nums[j]]

            
ans = Solution().twoSum([2,7,11,15], 9)
print(ans)