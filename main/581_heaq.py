import heapq
from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        pq = nums.copy()
        heapq.heapify(pq)

        i = 0
        while len(pq) > 0 and pq[0] == nums[i]:
            heapq.heappop(pq)
            i += 1
        
        i = len(nums) - 1
        pq = [-x for x in pq]
        heapq.heapify(pq)
        while len(pq) > 0 and -pq[0] == nums[i]:
            heapq.heappop(pq)
            i -= 1

        return len(pq)

        
cases = [
    [2,6,4,8,10,9,15],
    [1,2,3,4],
    [1]
]

for case in cases:
    ans = Solution().findUnsortedSubarray(case)
    print(ans)