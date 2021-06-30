from typing import List

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)

        dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max([dp[i-1][j], dp[i][j-1], dp[i-1][j-1]])
        return dp[m][n]


x = Solution()
ans = x.maxUncrossedLines([1,4,2], [1,2,4])
print(ans)
ans = x.maxUncrossedLines([2,5,1,2,5], [10,5,2,1,5,2])
print(ans)
ans = x.maxUncrossedLines([1,3,7,1,7,5], [1,9,2,5,1])
print(ans)
ans = x.maxUncrossedLines([1], [3])
print(ans)
ans = x.maxUncrossedLines([2,1], [1,2,1,3,3,2])
print(ans)
ans = x.maxUncrossedLines([1,1,3,5,3,3,5,5,1,1], [2,3,2,1,3,5,3,2,2,1])
print(ans)