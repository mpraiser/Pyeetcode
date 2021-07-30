class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        base = 1
        ret = 0
        for c in reversed(columnTitle):
            ret += base * (ord(c) - ord("A") + 1)
            base *= 26
        return ret


def number2title(n: int) -> str:
    ret = ""
    while n > 0:
        n, r = divmod(n-1, 26)
        ret = chr(ord("A") + r) + ret
    return ret


# for i in range(28):
#     print(number2title(i))


cases = [
    "A",
    "AB",
    "ZY",
    "FXSHRXW"
]
for case in cases:
    ans = Solution().titleToNumber(case)
    print(ans)
        