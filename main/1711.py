from typing import List


class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        def f(n):
            t = 2 ** n
            result = 0
            another = dict()
            for a in deliciousness:
                if a in another:
                    result += another[a]
                b = t - a
                if b in another:
                    another[b] += 1
                else:
                    another[b] = 1
            return result % (10 ** 9 + 7)
        return sum((f(i) for i in range(41))) % (10 ** 9 + 7)


ans = Solution().countPairs([1,1,1,3,3,3,7])
print(ans)