from typing import List, Set, Deque, Tuple
from collections import deque


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:

        def bfs(g: List[List[int]]):
            n = len(g)
            q: Deque[Tuple] = deque(
                (i, 1 << i, 0) for i in range(n)
            )  # (node, mask, dist)
            visited: Set[Tuple] = set(
                (i, 1 << i) for i in range(n)
            )  # (node, mask)

            while q:
                u, mask_u, dist_u = q.popleft()
                if mask_u == (1 << n) - 1:
                    # mask为n个1： 1111 1111 1111
                    # 标志所有节点都被访问过了
                    return dist_u
                for v in g[u]:
                    mask_v = mask_u | 1 << v
                    if (v, mask_v) not in visited:
                        dist_v = dist_u + 1
                        q.append((v, mask_v, dist_v))
                        visited.add((v, mask_v))
            return -1

        return bfs(graph)


cases = [
    [[1, 2, 3], [0], [0], [0]],
    [[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]
]

for case in cases:
    ans = Solution().shortestPathLength(case)
    print(ans)

# ans = Solution().shortestPathLength(cases[1])
# print(ans)