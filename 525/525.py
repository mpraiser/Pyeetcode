from typing import List
from itertools import accumulate


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        converted_nums = [-1 if i == 0 else 1 for i in nums]

        sums = list(accumulate(converted_nums))
        sums2index = {}

        max_distance = 0

        for i, s in enumerate(sums):
            if s == 0 and i > max_distance:
                max_distance = i + 1
            else:
                if s in sums2index:
                    if (distance := i - sums2index[s]) > max_distance:
                        max_distance = distance
                else:
                    sums2index[s] = i
        return max_distance


x = Solution()
ans = x.findMaxLength([0,1,0])
# ans = x.findMaxLength([0,0, 0, 1, 1, 1 , 1, 0, 0, 0, 0])
# ans = x.findMaxLength([0, 1])
print(ans)