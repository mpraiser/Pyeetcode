import functools
from typing import List

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        @functools.lru_cache(maxsize=None)
        def xor_range(x, y):
            """
            return xor of element in [x, y)
            """
            if x == y:
                return arr[x]
            else:
                if x == 0:
                    if y == 1:
                        return arr[0]
                    else:
                        return xor_range(0, y-1) ^ arr[y-1]
                else:
                    return xor_range(0, y) ^ xor_range(0, x)

        count = 0
        for i in range(len(arr) - 1):
            for j in range(i+1, len(arr)):
                for k in range(j, len(arr)):
                    if xor_range(i, j) == xor_range(j, k+1):
                        count += 1

        return count


x = Solution()
# ans = x.countTriplets([2,3,1,6,7])
ans = x.countTriplets([7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7])
print(ans)