from typing import List
from collections import deque


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # preprocess: use adjacency matrix to decribe graph
        graph = [[float("inf") for _ in range(n)] for _ in range(n)]
        # [1, n] -> [0, n)
        for u, v, w in times:
            graph[u-1][v-1] = w
        
        uncertain = set(range(n))
        visited = [float("inf") for _ in range(n)] # time to reach node
        visited[k-1] = 0
        while len(uncertain) > 0:
            u = min(uncertain, key=lambda x: visited[x])  # argmin of visited[u]
            uncertain.remove(u)
            t_u = visited[u]
            for v in uncertain:
                t_v = t_u + graph[u][v]
                if t_v < visited[v]:
                    visited[v] = t_v
        ans = max(visited)
        return ans if ans < float("inf") else -1


cases = [
    ([[2,1,1],[2,3,1],[3,4,1]], 4, 2),
    ([[1,2,1]], 2, 1),
    ([[1,2,1]], 2, 2),
    ([[1,2,1],[2,1,3]], 2, 2),
    ([[1,2,1],[2,3,2],[1,3,2]], 3, 1)
]

for case in cases:
    ans = Solution().networkDelayTime(*case)
    print(ans)

# ans = Solution().networkDelayTime(*cases[0])
# print(ans)

