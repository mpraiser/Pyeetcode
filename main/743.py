from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # preprocess
        graph = dict()
        for u, v, w in times:
            if u not in graph:
                graph[u] = dict()
            graph[u][v] = w
        
        visited = dict()  # time to reach node

        def dfs(u, t=0) -> int:
            nonlocal visited
            visited[u] = t
            if u in graph:
                for v in graph[u]:
                    t_next = t + graph[u][v]
                    if (v not in visited) or visited[v] > t_next:
                        dfs(v, t_next)

        dfs(k, 0)
        if len(visited) == n:
            return max(visited[node] for node in visited)
        else:
            return -1


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

# ans = Solution().networkDelayTime(*cases[4])
# print(ans)

