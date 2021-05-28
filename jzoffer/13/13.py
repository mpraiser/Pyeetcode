import functools


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        @functools.cache
        def sum_of_bits(x: int):
            return sum((int(i) for i in str(x)))

        @functools.cache
        def valid(a: int, b: int):
            return sum_of_bits(a) + sum_of_bits(b) <= k

        cache = {}

        def dfs(a, b):
            """
            check if (a, b) is reachable
            and search 4 directions from (a, b)
            """
            if (a, b) not in cache:
                if (not 0 <= a < m) or (not 0 <= b < n) or (not valid(a, b)):
                    cache[(a, b)] = False
                    return
                else:
                    cache[(a, b)] = True
                    dfs(a+1, b)
                    dfs(a, b+1)
                    dfs(a-1, b)
                    dfs(a, b-1)

        dfs(0, 0)
        count = sum((1 for p in cache if cache[p]))
        return count

x = Solution()
ans = x.movingCount(16, 8, 4)
print(ans)