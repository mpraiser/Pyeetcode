from typing import List
from collections import deque


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        dq = deque(nums)
        
        while len(dq) > 0 and dq[0] == min(dq):
            dq.popleft()
        
        while len(dq) > 0 and dq[-1] == max(dq):
            dq.pop()

        return len(dq)

        
cases = [
    [2,6,4,8,10,9,15],
    [1,2,3,4],
    [1]
]

for case in cases:
    ans = Solution().findUnsortedSubarray(case)
    print(ans)