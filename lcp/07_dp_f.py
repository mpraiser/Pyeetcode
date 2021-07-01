from typing import List
from functools import cache


class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        @cache
        def f(i, j):
            """number of solutions that reach j in i steps"""
            if i == 0:
                if j == 0:
                    return 1
                else:
                    return 0

            ans = 0
            for edge in relation:
                src = edge[0]
                dst = edge[1]
                if dst == j:
                    ans += f(i - 1, src)
            return ans
        return f(k, n-1)


ans = Solution().numWays(5, [[0,2],[2,1],[3,4],[2,3],[1,4],[2,0],[0,4]], 3)
print(ans)