from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        counter = {}
        for i in nums:
            if i not in counter:
                counter[i] = 1
            else:
                return i
