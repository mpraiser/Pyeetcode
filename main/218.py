import heapq
from typing import List


class MaxHeap:
    def __init__(self, values: List):
        self.__pq = values if values else []
        heapq.heapify(self.__pq)
    
    def push(self, item):
        heapq.heappush(self.__pq, -item)
    
    def pop(self):
        return -heapq.heappop(self.__pq)

    def remove(self, item):
        self.__pq.remove(-item)
        heapq.heapify(self.__pq)

    def top(self):
        return -self.__pq[0]


class Solution:
    # this problem is to get all **left point** of skyline
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # get all critical points, and sort by x-coordinate
        criticals = []
        for (l, r, h) in buildings:
            criticals.append((l, -h))
            criticals.append((r, h))
        # sort trick:
        # 1. sort by x-coordinate
        # 2. left point < right point
        # 3. if x is same, left points sorted from higher to lower
        #       right points sorted from lower to higher
        # the sequence of height allows only the highest point will be added to answer, according to the direction of traversal.
        criticals.sort()

        last_h = 0
        pq = MaxHeap([0])

        # line sweep
        res = []
        for (x, h) in criticals:
            if h <= 0:
                pq.push(-h)
            else:
                pq.remove(h)
            
            this_h = pq.top()
            if this_h != last_h:
                res.append([x, this_h])
                last_h = this_h
        return res


cases = [
    [[1,2,1],[1,2,2],[1,2,3]],
    [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
]

ans = Solution().getSkyline(cases[0])
print(ans)