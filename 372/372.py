class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        assert 1 <= columnNumber
        n = columnNumber
        result = ""
        while n > 0:
            n, low = divmod(n - 1, 26)
            result = chr(ord('A') + low) + result
        return result


cases = [1, 28, 701, 2147483647]
for case in cases:
    ans = Solution().convertToTitle(case)
    print(ans)
