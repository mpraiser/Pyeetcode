import heapq
from typing import List


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        """
        k <= len(arr)
        """
        mins = []

        for n in arr:
            heapq.heappush(mins, n)

        result = []

        for i in range(k):
            result.append(heapq.heappop(mins))

        return result
            