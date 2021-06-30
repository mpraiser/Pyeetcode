from typing import List


def digits2int(digits) -> int:
    base = 1
    result = 0
    for d in digits:
        result += base * d
        base *= 10
    return result


def int2digits(x: int, *, reverse=False) -> List[int]:
    r = [int(i) for i in str(x)]
    return list(reversed(r)) if reverse else r


class Solution:
    def countDigitOne(self, n: int) -> int:
        digits = int2digits(n, reverse=True)
        counter = 0
        for i, cur in enumerate(digits):
            # print(counter)
            # high
            counter += digits2int(digits[i+1:]) * (10 ** i)
            # low
            if cur >= 2:
                counter += 10 ** i
            elif cur == 1:
                counter += digits2int(digits[:i]) + 1
        return counter


cases = [0, 5, 12, 13, 20, 100]

for case in cases:
    ans = Solution().countDigitOne(case)
    print(ans)

# ans = Solution().countDigitOne(100)
# print(ans)