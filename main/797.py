from functools import cache


class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        n = len(graph)

        @cache
        def dfs(node: int) -> list[list[int]]:
            result = []
            if node == n - 1:
                result.append([node])
            else:
                for child in graph[node]:
                    solutions = dfs(child)
                    for sol in solutions:
                        result.append([node] + sol)
            return result

        return dfs(0)


cases = [
    [[1, 2], [3], [3], []],
    [[4, 3, 1], [3, 2, 4], [3], [4], []]
]
for case in cases:
    ans = Solution().allPathsSourceTarget(case)
    print(ans)
