from typing import List
from itertools import combinations, product


def n_bits_one(ones: int, n: int):
    index = (i for i in range(n))
    for ptrs in combinations(index, ones):
        r = sum((1 << p for p in ptrs))
        yield r


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []
        for h in range(turnedOn + 1):
            m = turnedOn - h
            hours = filter(lambda hour: 0 <= hour < 12, n_bits_one(h, 4))
            mins = filter(lambda min: 0 <= min < 60, n_bits_one(m, 6))
            for pair in product(hours, mins):
                result.append(f"{pair[0]}:{pair[1]:02d}")
        return result


ans = Solution().readBinaryWatch(1)
print(ans)
