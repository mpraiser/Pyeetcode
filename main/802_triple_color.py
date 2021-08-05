from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        state = [0] * len(graph)
        # 0: not processed
        # 1: processing or a ring appears (means failure)
        # 2: success

        def safe(u) -> bool:
            nonlocal state
            if state[u] > 0:
                return state[u] == 2  # implicit the idea of 'safe'
            state[u] = 1  # process this node
            for v in graph[u]:
                if not safe(v):
                    return False
            state[u] = 2
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

# ans = Solution().eventualSafeNodes(cases[2])
# print(ans)
