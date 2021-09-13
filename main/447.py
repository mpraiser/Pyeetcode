from collections import Counter


class Solution:
    def numberOfBoomerangs(self, points: list[list[int]]) -> int:
        count = 0
        for p in points:
            dist = Counter(
                map(
                    lambda q: (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2,
                    points
                )
            )
            for d in dist.values():
                count += d * (d - 1)
        return count


ans = Solution().numberOfBoomerangs([[0, 0], [1, 0], [2, 0]])
print(ans)
