from typing import List, Optional


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        cache = dict()

        def f(src) -> bool:
            nonlocal cache
            if src in cache:
                return cache[src]

            cache[src] = None  # mark this node as it's being processed

            ret = True
            for dst in graph[src]:
                if dst in cache and (not cache[dst]):
                    # if cache[src] is True, ret = ret and cache[dst] has no effect.
                    # if cache[src] is None, it means a ring appears, which is not acceptable.
                    # if cache[src] is False, means this node is not safe.
                    cache[src] = False
                    return False
                else:
                    ret = ret and f(dst)

            cache[src] = ret
            return ret

        result = [i for i in range(len(graph)) if f(i)]
        return result


cases = [
    [[1, 2], [2, 3], [5], [0], [5], [], []],
    [[1,2,3,4],[1,2],[3,4],[0,4],[]],
    [[],[0,2,3,4],[3],[4],[]]
]

for case in cases:
    ans = Solution().eventualSafeNodes(case)
    print(ans)

# ans = Solution().eventualSafeNodes(cases[2])
# print(ans)