from math import log, ceil


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and ceil(tmp:=log(n, 4)) == tmp


x = Solution()
ans = x.isPowerOfFour(16)
print(ans)