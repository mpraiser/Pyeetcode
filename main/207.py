from functools import partial, reduce


class Solution:
    @staticmethod
    def imperative(n: int, graph: list[list[int]]) -> bool:
        cache: dict[int, bool] = {}
        # 3 possible states:
        #   not in cache: not visited
        #   False: visiting / ring
        #   Ture: visited

        def no_ring(src: int) -> bool:
            nonlocal graph, cache
            if src in cache:
                return cache[src]
            cache[src] = False
            ret = all(no_ring(dst) for dst in graph[src])
            cache[src] = ret
            return ret

        return all(no_ring(i) for i in range(n))

    @staticmethod
    def functional(n: int, graph: list[list[int]]) -> bool:
        def config(s: tuple[int], i: int, value: int) -> tuple[int]:
            s = list(s)
            s[i] = value
            return tuple(s)

        def no_ring(g: list[list[int]], s: tuple[int], u: int) -> tuple[int]:
            if s[u] != 0:
                return s

            s = config(s, u, 1)
            s = reduce(
                partial(no_ring, g),
                graph[u],  # why Pycharm says type is wrong here?
                s
            )
            if all(s[i] == 2 for i in graph[u]):
                s = config(s, u, 2)
            return s

        initial = tuple(0 for _ in range(n))
        final = reduce(
            partial(no_ring, graph),
            range(n),
            initial
        )
        return all(final[i] == 2 for i in range(n))

    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # preprocess to adjacency graph
        graph = [[] for _ in range(numCourses)]
        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)
        return self.functional(numCourses, graph)


cases = [
    (2, [[1, 0]]),
    (2, [[1, 0], [0, 1]]),
    (5, [[1, 4], [2, 4], [3, 1], [3, 2]]),
    (7, [[1, 0], [0, 3], [0, 2], [3, 2], [2, 5], [4, 5], [5, 6], [2, 4]])
]
for case in cases:
    ans = Solution().canFinish(*case)
    print(ans)

# ans = Solution().canFinish(*cases[2])
# print(ans)
