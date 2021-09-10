class Solution:
    def chalkReplacer(self, chalk: list[int], k: int) -> int:
        total = sum(chalk)
        k %= total
        for i, c in enumerate(chalk):
            if k < c:
                return i
            else:
                k -= c


cases = [
    ([5, 1, 5], 22),
    ([3, 4, 1, 2], 25)
]
for case in cases:
    ans = Solution().chalkReplacer(*case)
    print(ans)
