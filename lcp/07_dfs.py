from typing import List


class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        childs = dict()
        for x in relation:
            parent, child = x[0], x[1]
            if x[0] not in childs:
                childs[parent] = set()
            childs[parent].add(child)

        ans = 0

        def dfs(parent, depth):
            nonlocal ans
            if depth == k:
                if parent == n-1:
                    ans += 1
                return
            
            if parent in childs:
                for child in childs[parent]:
                    dfs(child, depth + 1)

        dfs(0, 0)
        return ans


ans = Solution().numWays(5, [[0,2],[2,1],[3,4],[2,3],[1,4],[2,0],[0,4]], 3)
print(ans)