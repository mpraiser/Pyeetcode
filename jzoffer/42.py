from typing import List, Tuple


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def dp():
            last = nums[0]
            yield last
            for i in range(1, len(nums)):          
                last = nums[i] + max(last, 0)
                yield last
        return max(dp())


ans = Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(ans)