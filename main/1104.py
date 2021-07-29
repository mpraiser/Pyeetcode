from typing import List
from math import log2, floor


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        ret = []
        # every layer is [2 ** (n-1), 2 ** n)
        layer: int = floor(log2(label)) + 1
        right = 2 ** layer
        left = right // 2

        while True:
            ret.append(label)
            if layer <= 1:
                break
            # prepare next iter
            # in even line, reverse it
            if layer % 2 == 0:
                label = right - 1 - (label - left)
            # get parent label
            label //= 2
            layer -= 1
            right = left
            left //= 2
            # in even line, reverse it
            if layer % 2 == 0:
                label = right - 1 - (label - left)
 
        return ret[::-1]


cases = [
    14,
    26,
    1
]


for case in cases:
    ans = Solution().pathInZigZagTree(case)
    print(ans)