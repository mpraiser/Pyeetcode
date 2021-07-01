from typing import List


class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        dp = [[0] * n for _ in range(k+1)]
        dp[0][0] = 1
        for i in range(k):
            for edge in relation:
                src, dst = edge[0], edge[1]
                dp[i+1][dst] += dp[i][src]
        return dp[k][n - 1]


ans = Solution().numWays(5, [[0,2],[2,1],[3,4],[2,3],[1,4],[2,0],[0,4]], 3)
print(ans)