from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        right = len(citations)
        while left < right:
            mid = (left + right) // 2
            if citations[mid] >= len(citations) - mid:
                right = mid
            else:
                left = mid + 1
        return len(citations) - right


cases = [
    [0],
    [1],
    [0, 0],
    [0,1,3,5,6]
]

for case in cases:
    ans = Solution().hIndex(case)
    print(ans)

# ans = Solution().hIndex(cases[2])
# print(ans)