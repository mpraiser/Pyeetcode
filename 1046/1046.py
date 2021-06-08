import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = [-x for x in stones]
        heapq.heapify(pq)

        while len(pq) > 1:
            x = heapq.heappop(pq)
            y = heapq.heappop(pq)
            if x != y:
                heapq.heappush(pq, -abs(x - y))
        
        return -pq[0] if pq else 0


x = Solution()
ans = x.lastStoneWeight([2,7,4,1,8,1])
# ans = x.lastStoneWeight([31,26,33,21,40])
print(ans)