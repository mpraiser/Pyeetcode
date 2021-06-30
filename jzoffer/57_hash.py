from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        another = set([target - n for n in nums])
        for n in nums:
            if n in another:
                return [n, target-n]
            
            
ans = Solution().twoSum([2,7,11,15], 9)
print(ans)