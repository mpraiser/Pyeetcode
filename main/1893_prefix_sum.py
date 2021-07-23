from typing import List


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        SIZE = 50 + 1
        BIAS = 1
        diff = [0] * SIZE
        for l, r in ranges:
            diff[l-BIAS] += 1
            diff[r+1-BIAS] -= 1

        psum = 0
        for i in range(BIAS, left):
            psum += diff[i-BIAS]

        for i in range(left, right+1):
            psum += diff[i-BIAS]
            if psum <= 0:
                return False
        return True
            
        


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