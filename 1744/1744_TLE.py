from typing import List, Tuple


class Candies:
    def __init__(self, count):
        self.count = count.copy()
    
    def __sub__(self, x: int):
        i = 0
        while x > 0 and i < len(self.count):
            if self.count[i] >= x:
                self.count[i] -= x
                x = 0
            else:
                x -= self.count[i]
                self.count[i] = 0
                i += 1
        return self

    def __le__(self, other):
        res = self.count[::-1] <= other.count[::-1]
        return res

    def __repr__(self):
        return str(self.count)


class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        def can(f_type, f_day, cap) -> bool:
            c_hi = Candies(candiesCount) - f_day * 1
            c_lo = Candies(candiesCount) - f_day * cap

            t_hi = candiesCount.copy()
            t_lo = candiesCount.copy()
            for i in range(f_type):
                t_lo[i] = 0
            t_lo[f_type] = 1

            if f_type >= 1:
                ptr = f_type - 1
                compensate = cap -1
                while compensate > 0 and ptr >= 0:
                    if compensate > t_hi[ptr]:
                        compensate -= t_hi[ptr]
                    else:
                        t_hi[ptr] = compensate
                        compensate = 0
                    ptr -= 1
                for i in range(ptr+1):
                    t_hi[i] = 0

            t_hi = Candies(t_hi)
            t_lo = Candies(t_lo)

            print(candiesCount[::-1])
            print(c_lo.count[::-1])
            print(c_hi.count[::-1])

            print(t_lo.count[::-1])
            print(t_hi.count[::-1])
    
            return c_lo <= t_hi and t_lo <= c_hi

        results = [can(*q) for q in queries]
        return results


x = Solution()
# ans = x.canEat([7,4,5,3,8], [[0,2,2],[4,2,4],[2,13,1000000000]])
# ans = x.canEat([5,2,6,4,1], [[3,1,2],[4,10,3],[3,10,100],[4,100,30],[1,3,1]])
# ans = x.canEat([5,2,6,4,1], [[1,3,1]])
# ans = x.canEat([46,5,47,48,43,34,15,26,11,25,41,47,15,25,16,50,32,42,32,21,36,34,50,45,46,15,46,38,50,12,3,26,26,16,23,1,4,48,47,32,47,16,33,23,38,2,19,50,6,19,29,3,27,12,6,22,33,28,7,10,12,8,13,24,21,38,43,26,35,18,34,3,14,48,50,34,38,4,50,26,5,35,11,2,35,9,11,31,36,20,21,37,18,34,34,10,21,8,5], [[85,54,42]])
# ans = x.canEat([10,11,42,42,49,14,44,33,13,49,32,19,48,36,25,38,32,45,30,21,13,45,39,12,12,25,26,18,35,28,1,31,14,16,38,49,26,33,39,39,7,31,20,8,49,36,6,1,32,2,35,10,31,37,13,43,26], [[52, 19, 44]])
ans = x.canEat(a, b)
print(ans)