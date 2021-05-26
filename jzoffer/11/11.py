from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        result = numbers[0]
        for i, x in enumerate(numbers):
            j = (i+1) % len(numbers)
            if numbers[i] > numbers[j]:
                result = numbers[j]
                break
        return result


x = Solution()
ans = x.minArray([2,2,2,0,1])
print(ans)