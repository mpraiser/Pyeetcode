from typing import List


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        # greedy
        # i = 0
        arr.sort()
        arr[0] = 1
        # i >= 1
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1] + 1:
                arr[i] = arr[i-1] + 1
        return max(arr)


ans = Solution().maximumElementAfterDecrementingAndRearranging([1,100,1000])
print(ans)