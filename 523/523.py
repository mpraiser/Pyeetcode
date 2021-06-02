from typing import List
from itertools import accumulate


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        sums = list(accumulate(nums))

        def f(i, j):
            """
            sum of nums in [i, j]
            """
            if i == 0:
                return sums[j]
            else:
                return sums[j] - sums[i]

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if f(i, j) % k == 0:
                    return True
        return False


x = Solution()
ans = x.checkSubarraySum([23,2,4,6,7], 6)
print(ans)