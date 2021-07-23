from typing import List


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        r = set()
        for x in ranges:
            r |= set(range(x[0], x[1] + 1))
        return set(range(left, right + 1)).issubset(r)


cases = [
    ([[1,2],[3,4],[5,6]], 2, 5),
    ([[1,10],[10,20]], 21, 21),
    ([[1,1]], 1, 50)
]

for case in cases:
    ans = Solution().isCovered(*case)
    print(ans)

# ans = Solution().isCovered(*cases[2])
# print(ans)