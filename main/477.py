import functools
from typing import List


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for i in range(30):
            c = sum(((num >> i) & 1 for num in nums))
            total += c * (n-c)
        return total


x = Solution()
ans = x.totalHammingDistance([4, 14, 2])
print(ans)