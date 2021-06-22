def digits2int(digits) -> int:
    base = 1
    result = 0
    for d in digits:
        result += base * d
        base *= 10
    return result


def int2digits(x: int, *, reverse=False) -> List[int]:
    r = [int(i) for i in str(x)]
    return reversed(r) if reverse else r


class Solution:
    def countDigitOne(self, n: int) -> int:
        def f(i, j):
            """[i, j)"""

        return f(0, n+1)


cases = [0, 5, 11, 13, 20, 100]

for case in cases:
    ans = Solution().countDigitOne(case)
    print(ans)

# ans = Solution().countDigitOne(11)
# print(ans)