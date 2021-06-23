from typing import List


def int2digits(x: int, *, reverse=False) -> List[int]:
    r = [int(i) for i in str(x)]
    return list(reversed(r)) if reverse else r

class Solution:
    def findNthDigit(self, n: int) -> int:
        if n < 10:
            return n
        n = n - 1
        i = 1
        while True:
            n_next = n - i * 9 * 10 ** (i-1)
            if n_next < 0:
                break
            n = n_next
            i += 1
        
        if n == 0:
            return 1
        # 第几个i进制数
        number = 10 ** (i-1) + n // i
        digits = int2digits(number)
        return digits[n % i]


cases = [3, 5, 11, 13, 19]

for case in cases:
    ans = Solution().findNthDigit(case)
    print(ans)


# ans = Solution().findNthDigit(13)
# print(ans)