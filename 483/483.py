class Solution:
    def smallestGoodBase(self, n: str) -> str:
        def f(k, m, n):
            return (k**m - 1) - (k - 1) * n
        n = int(n)
        for m in reversed(range(2, 61)):
            left = 2
            right = n
            while left <= right:
                mid = (left + right) // 2
                r = f(mid, m, n)
                if r == 0:
                    return str(mid)
                elif r < 0:
                    left = mid + 1
                elif r > 0:
                    right = mid - 1


ans = Solution().smallestGoodBase("1000000000000000000")
print(ans)