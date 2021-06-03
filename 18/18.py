from typing import List
from itertools import combinations

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        result = set()
        nums.sort()
        for a in range(len(nums)-3):
            for b in range(a+1, len(nums)-2):
                for c in range(b+1, len(nums)-1):
                    for d in range(c+1, len(nums)):
                        four = (nums[a], nums[b], nums[c], nums[d])
                        if sum(four) == target:
                            result.add(four)
        return [list(x) for x in result]

x = Solution()
# ans = x.fourSum([1,0,-1,0,-2,2], 0)
# ans = x.fourSum([2,2,2,2,2], 8)
ans = x.fourSum([-5,5,4,-3,0,0,4,-2], 4)
print(ans)