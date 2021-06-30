from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = dict()
        for i, x in enumerate(nums):
            if (y := target - x) in indices:
                return [i, indices[y]]
            indices[x] = i
        return []


ans = Solution().twoSum([2,7,11,15], 9)
print(ans)