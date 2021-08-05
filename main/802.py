from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        state = dict()

        def safe(u: int) -> bool:
            nonlocal state
            if u in state:
                return state[u]

            state[u] = False  # 标志节点被访问
            for v in graph[u]:
                if not safe(v):
                    return False
            state[u] = True
            return True

        result = [i for i in range(len(graph)) if safe(i)]
        return result


cases = [
    [[1, 2], [2, 3], [5], [0], [5], [], []],
    [[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []],
    [[], [0, 2, 3, 4], [3], [4], []]
]

for case in cases:
    ans = Solution().eventualSafeNodes(case)
    print(ans)

# ans = Solution().eventualSafeNodes(cases[0])
# print(ans)
