from typing import List
from math import floor

class Solution:
    def minArray(self, numbers: List[int]) -> int:
        left = 0
        right = len(numbers)-1
        while left < right:
            pivot = floor((left + right) // 2)
            if numbers[pivot] > numbers[right]:
                left = pivot + 1
            elif numbers[pivot] < numbers[right]:
                right = pivot
            else:
                right -= 1
        return numbers[left]


x = Solution()
ans = x.minArray([2,2,2,0,1])
print(ans)