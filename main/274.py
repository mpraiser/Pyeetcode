from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h = 0
        citations.sort(reverse=True)
        for x in citations:
            if x >= h + 1:
                h += 1
            else:
                break
        return h
        

cases = [
    [0],
    [1],
    [3,0,6,1,5]
]

for case in cases:
    ans = Solution().hIndex(case)
    print(ans)