from typing import List, Tuple
from itertools import accumulate


class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        index = list(accumulate(candiesCount))

        def can(f_type, f_day, cap) -> bool:
            # total number of eat on f_day
            min_eat = f_day + 1
            max_eat = (f_day + 1) * cap

            # remember to plus 1: from index i to number i
            min_fav = index[f_type-1] + 1 if f_type >= 1 else 0
            max_fav = index[f_type]
            return min_eat <= max_fav and max_eat >= min_fav

        results = [can(*q) for q in queries]
        return results


x = Solution()
# ans = x.canEat([7,4,5,3,8], [[0,2,2],[4,2,4],[2,13,1000000000]])
# ans = x.canEat([5,2,6,4,1], [[3,1,2],[4,10,3],[3,10,100],[4,100,30],[1,3,1]])
ans = x.canEat([7,11,5,3,8], [[2,2,6],[4,2,4],[2,13,1000000000]])
# ans = x.canEat([46,5,47,48,43,34,15,26,11,25,41,47,15,25,16,50,32,42,32,21,36,34,50,45,46,15,46,38,50,12,3,26,26,16,23,1,4,48,47,32,47,16,33,23,38,2,19,50,6,19,29,3,27,12,6,22,33,28,7,10,12,8,13,24,21,38,43,26,35,18,34,3,14,48,50,34,38,4,50,26,5,35,11,2,35,9,11,31,36,20,21,37,18,34,34,10,21,8,5], [[85,54,42]])
# ans = x.canEat([10,11,42,42,49,14,44,33,13,49,32,19,48,36,25,38,32,45,30,21,13,45,39,12,12,25,26,18,35,28,1,31,14,16,38,49,26,33,39,39,7,31,20,8,49,36,6,1,32,2,35,10,31,37,13,43,26], [[52, 19, 44]])
# ans = x.canEat(a, b)
print(ans)